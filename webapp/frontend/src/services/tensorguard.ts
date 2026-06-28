import type {
  ApiDetailPayload,
  ApiJobPayload,
  ApiListItem,
  ApiRunStartInput,
  CandidateCreateInput,
  CandidateDetail,
  CandidateRecord,
  CandidateUpdateInput,
  ConfirmedBugDetail,
  ConfirmedBugSummary,
  EnvironmentPayload,
  JobStartPayload,
  Library,
  OverviewPayload,
  ReplayStartInput,
  ReproJobPayload,
  ReproReportPayload,
} from "../types/tensorguard";
import { request } from "./http";

export const endpoints = {
  overview: "/api/overview",
  environment: "/api/environment",
  apis: "/api/apis",
  apiDetail: "/api/api-detail",
  runApi: "/api/run-api",
  apiJob: (id: string) => `/api/api-jobs/${encodeURIComponent(id)}`,
  candidates: "/api/candidates",
  candidate: (id: string) => `/api/candidates/${encodeURIComponent(id)}`,
  candidateStatus: (id: string) => `/api/candidates/${encodeURIComponent(id)}/status`,
  confirmedBugs: "/api/confirmed-bugs",
  confirmedBug: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}`,
  reproduce: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}/reproduce`,
  reproJob: (id: string) => `/api/repro-jobs/${encodeURIComponent(id)}`,
  reproReport: (id: string) => `/api/repro-jobs/${encodeURIComponent(id)}/report`,
} as const;

function withQuery(path: string, values: Record<string, string | number>): string {
  const query = new URLSearchParams();
  for (const [key, value] of Object.entries(values)) {
    query.set(key, String(value));
  }
  return `${path}?${query.toString()}`;
}

function get<T>(path: string): Promise<T> {
  return request<T>(path, { method: "GET" });
}

function post<T>(path: string, body?: unknown): Promise<T> {
  return request<T>(path, {
    method: "POST",
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
}

export function getOverview(): Promise<OverviewPayload> {
  return get(endpoints.overview);
}

export function getEnvironment(refresh = false): Promise<EnvironmentPayload> {
  const path = refresh ? withQuery(endpoints.environment, { refresh: 1 }) : endpoints.environment;
  return get(path);
}

export function getApis(lib: Library, query = "", limit = 200): Promise<ApiListItem[]> {
  return get(withQuery(endpoints.apis, { lib, q: query, limit }));
}

export function getApiDetail(lib: Library, api: string): Promise<ApiDetailPayload> {
  return get(withQuery(endpoints.apiDetail, { lib, api }));
}

export function startApiRun(input: ApiRunStartInput): Promise<JobStartPayload> {
  return post(endpoints.runApi, { lib: input.lib, api: input.api, mode: input.mode });
}

export function getApiJob(id: string): Promise<ApiJobPayload> {
  return get(endpoints.apiJob(id));
}

export function getCandidates(): Promise<CandidateRecord[]> {
  return get(endpoints.candidates);
}

export function createCandidate(input: CandidateCreateInput): Promise<CandidateRecord> {
  return post(endpoints.candidates, input);
}

export function getCandidate(id: string): Promise<CandidateDetail> {
  return get(endpoints.candidate(id));
}

export function updateCandidateStatus(id: string, input: CandidateUpdateInput): Promise<CandidateRecord> {
  return post(endpoints.candidateStatus(id), input);
}

export function getConfirmedBugs(): Promise<ConfirmedBugSummary[]> {
  return get(endpoints.confirmedBugs);
}

export function getConfirmedBug(id: string): Promise<ConfirmedBugDetail> {
  return get(endpoints.confirmedBug(id));
}

export function reproduceConfirmedBug(id: string, input: ReplayStartInput): Promise<JobStartPayload> {
  return post(endpoints.reproduce(id), input);
}

export function getReproJob(id: string): Promise<ReproJobPayload> {
  return get(endpoints.reproJob(id));
}

export function getReproReport(id: string): Promise<ReproReportPayload> {
  return get(endpoints.reproReport(id));
}

export function generateReproReport(id: string): Promise<ReproReportPayload> {
  return post(endpoints.reproReport(id));
}
