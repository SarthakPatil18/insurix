/**
 * Insurixx API Client
 * Centralized fetch handler with health probing, structured errors, and offline fallback.
 */

const API_BASE_URL = ''; // Relative URL leverages Vite proxy in dev, direct in prod

export interface ApiError {
  status: number;
  message: string;
  detail?: any;
}

let isBackendLive: boolean | null = null;

export async function probeBackendHealth(): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
      headers: { 'Accept': 'application/json' },
      signal: AbortSignal.timeout(2000),
    });
    isBackendLive = res.ok;
    return isBackendLive;
  } catch (e) {
    isBackendLive = false;
    return false;
  }
}

export function getCachedBackendStatus(): boolean | null {
  return isBackendLive;
}

export async function apiRequest<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const headers = new Headers(options.headers || {});
  if (!headers.has('Accept')) {
    headers.set('Accept', 'application/json');
  }

  // Auto-inject JSON Content-Type if body is object and not FormData
  if (options.body && !(options.body instanceof FormData) && !headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  const res = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!res.ok) {
    let errorDetail: any;
    try {
      errorDetail = await res.json();
    } catch {
      errorDetail = await res.text();
    }
    const err: ApiError = {
      status: res.status,
      message: errorDetail?.detail || errorDetail?.message || `HTTP ${res.status}: Request failed`,
      detail: errorDetail,
    };
    throw err;
  }

  if (res.status === 204) {
    return null as unknown as T;
  }

  return res.json() as Promise<T>;
}
