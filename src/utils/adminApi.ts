/** Admin API base URL for website form submissions (no trailing slash). */
export const ADMIN_API_BASE_URL = (
  import.meta.env.PUBLIC_ADMIN_API_URL?.trim() || 'https://live.panunkaergar.com'
).replace(/\/$/, '');
