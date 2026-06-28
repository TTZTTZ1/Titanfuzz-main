import { onBeforeUnmount, ref } from "vue";

export interface PollOutcome<T> {
  value: T;
  continue: boolean;
}

export function usePolling<T>(task: () => Promise<PollOutcome<T>>, intervalMs = 1000) {
  const latest = ref<T | null>(null);
  const running = ref(false);
  const loading = ref(false);
  const error = ref<string | null>(null);

  let timer: ReturnType<typeof setTimeout> | null = null;
  let requestToken = 0;
  let inFlight = false;

  function describeError(value: unknown): string {
    if (value instanceof Error) {
      return value.message;
    }

    return "轮询失败";
  }

  function clearTimer() {
    if (timer !== null) {
      clearTimeout(timer);
      timer = null;
    }
  }

  function stop() {
    running.value = false;
    loading.value = false;
    requestToken += 1;
    clearTimer();
  }

  function schedule(delay: number) {
    clearTimer();
    timer = setTimeout(() => {
      timer = null;
      void tick();
    }, delay);
  }

  async function tick() {
    if (!running.value || inFlight) {
      return;
    }

    const token = requestToken;
    inFlight = true;
    loading.value = true;

    try {
      const outcome = await task();
      if (token !== requestToken || !running.value) {
        return;
      }

      latest.value = outcome.value;
      error.value = null;

      if (outcome.continue) {
        schedule(intervalMs);
      } else {
        stop();
      }
    } catch (cause) {
      if (token === requestToken) {
        error.value = describeError(cause);
        stop();
      }
    } finally {
      inFlight = false;
      if (token === requestToken && !running.value) {
        loading.value = false;
      } else if (token === requestToken) {
        loading.value = false;
      }
    }
  }

  function start() {
    if (running.value) {
      return;
    }

    requestToken += 1;
    running.value = true;
    error.value = null;
    schedule(0);
  }

  onBeforeUnmount(() => {
    stop();
  });

  return {
    latest,
    running,
    loading,
    error,
    start,
    stop,
  };
}
