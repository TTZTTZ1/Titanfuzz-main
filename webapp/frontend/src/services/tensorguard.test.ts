import { afterEach, describe, expect, expectTypeOf, it, vi } from "vitest";

import type {
  ApiJobMetric,
  ApiJobParameters,
  ApiJobStatus,
  CudaInfo,
  EnvironmentPayload,
  FrameworkInfo,
  GpuInfo,
  GpuMetricSample,
  PlatformInfo,
  PythonInfo,
} from "../types/tensorguard";

import { ApiError, request } from "./http";
import {
  createCandidate,
  generateReproReport,
  getApiDetail,
  getApiJob,
  getApis,
  getCandidate,
  getCandidates,
  getConfirmedBug,
  getConfirmedBugs,
  getEnvironment,
  getOverview,
  getReproJob,
  getReproReport,
  reproduceConfirmedBug,
  startApiRun,
  updateCandidateStatus,
} from "./tensorguard";

afterEach(() => {
  vi.unstubAllGlobals();
});

function jsonResponse(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

describe("TensorGuard payload types", () => {
  it("matches structured environment and job telemetry payloads", () => {
    expectTypeOf<EnvironmentPayload["platform"]>().toEqualTypeOf<PlatformInfo>();
    expectTypeOf<EnvironmentPayload["python"]>().toEqualTypeOf<PythonInfo>();
    expectTypeOf<EnvironmentPayload["frameworks"]>().toEqualTypeOf<FrameworkInfo>();
    expectTypeOf<EnvironmentPayload["cuda"]>().toEqualTypeOf<CudaInfo>();
    expectTypeOf<EnvironmentPayload["gpus"]>().toEqualTypeOf<GpuInfo[]>();
    expectTypeOf<ApiJobStatus["parameters"]>().toEqualTypeOf<ApiJobParameters | undefined>();
    expectTypeOf<ApiJobMetric["gpu"]>().toEqualTypeOf<GpuMetricSample | undefined>();
  });
});

describe("TensorGuard API service", () => {
  it("encodes API search parameters", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse([]));
    vi.stubGlobal("fetch", fetchMock);

    await getApis("torch", "Tensor add&slice/[0]", 5000);

    expect(fetchMock).toHaveBeenCalledWith(
      "/api/apis?lib=torch&q=Tensor+add%26slice%2F%5B0%5D&limit=5000",
      expect.objectContaining({ method: "GET" }),
    );
  });

  it("preserves the existing run-api body", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({ job_id: "job-1", out: "demo_runs/job-1" }, 202));
    vi.stubGlobal("fetch", fetchMock);
    const input = { lib: "torch", api: "torch.add", mode: "demo", cuda_device: "0" } as const;

    await startApiRun(input);

    const [path, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(path).toBe("/api/run-api");
    expect(init.method).toBe("POST");
    expect(JSON.parse(String(init.body))).toEqual(input);
  });

  it("throws ApiError with status and backend error message", async () => {
    const payload = { error: "api not found" };
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(jsonResponse(payload, 404)));

    const error = await getApiDetail("torch", "missing.api").catch((reason: unknown) => reason);

    expect(error).toBeInstanceOf(ApiError);
    expect(error).toMatchObject({ status: 404, message: "api not found", payload });
  });

  it("uses the report endpoint for existing retrieval and generation", async () => {
    const fetchMock = vi.fn().mockImplementation(() =>
      Promise.resolve(
        jsonResponse({ job_id: "job/one", report_path: "report.md", report_markdown: "# Report", immutable: true }),
      ),
    );
    vi.stubGlobal("fetch", fetchMock);

    await getReproReport("job/one");
    await generateReproReport("job/one");

    expect(fetchMock).toHaveBeenNthCalledWith(
      1,
      "/api/repro-jobs/job%2Fone/report",
      expect.objectContaining({ method: "GET" }),
    );
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      "/api/repro-jobs/job%2Fone/report",
      expect.objectContaining({ method: "POST" }),
    );
  });

  it("wraps overview, environment, and encoded job routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await getOverview();
    await getEnvironment();
    await getEnvironment(true);
    await getApiJob("api/job 1");
    await getReproJob("repro/job 1");

    expect(fetchMock.mock.calls.map(([path]) => path)).toEqual([
      "/api/overview",
      "/api/environment",
      "/api/environment?refresh=1",
      "/api/api-jobs/api%2Fjob%201",
      "/api/repro-jobs/repro%2Fjob%201",
    ]);
  });

  it("wraps candidate collection, detail, creation, and status routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);
    const createInput = {
      job_id: "job-1",
      lib: "tf",
      api: "tf.add",
      category: "crash",
      source_path: "demo_runs/api_jobs/job-1/Results/tf/crash/tf.add_1.py",
      note: "review",
    } as const;
    const updateInput = { status: "needs_review", note: "inspect log" } as const;

    await getCandidates();
    await createCandidate(createInput);
    await getCandidate("CAND/1");
    await updateCandidateStatus("CAND/1", updateInput);

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/candidates", "GET"],
      ["/api/candidates", "POST"],
      ["/api/candidates/CAND%2F1", "GET"],
      ["/api/candidates/CAND%2F1/status", "POST"],
    ]);
    expect(JSON.parse(String((fetchMock.mock.calls[1][1] as RequestInit).body))).toEqual(createInput);
    expect(JSON.parse(String((fetchMock.mock.calls[3][1] as RequestInit).body))).toEqual(updateInput);
  });

  it("wraps confirmed bug list, detail, and reproduce routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);
    const replayInput = { modes: ["cpu", "gpu:0"], timeout: 45 } as const;

    await getConfirmedBugs();
    await getConfirmedBug("PAPER/1");
    await reproduceConfirmedBug("PAPER/1", replayInput);

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/confirmed-bugs", "GET"],
      ["/api/confirmed-bugs/PAPER%2F1", "GET"],
      ["/api/confirmed-bugs/PAPER%2F1/reproduce", "POST"],
    ]);
    expect(JSON.parse(String((fetchMock.mock.calls[2][1] as RequestInit).body))).toEqual(replayInput);
  });
});

describe("request", () => {
  it("defaults JSON content type while preserving supplied headers", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({ ok: true }));
    vi.stubGlobal("fetch", fetchMock);

    await request("/api/test", {
      headers: { "Content-Type": "application/problem+json", "X-Trace-Id": "trace-1" },
    });

    const headers = new Headers((fetchMock.mock.calls[0][1] as RequestInit).headers);
    expect(headers.get("Content-Type")).toBe("application/problem+json");
    expect(headers.get("X-Trace-Id")).toBe("trace-1");
  });

  it("uses a useful HTTP message for non-JSON errors", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(new Response("service unavailable", { status: 503, statusText: "Service Unavailable" })),
    );

    const error = await request("/api/test").catch((reason: unknown) => reason);

    expect(error).toBeInstanceOf(ApiError);
    expect(error).toMatchObject({ status: 503, message: "HTTP 503 Service Unavailable", payload: "service unavailable" });
  });
});
