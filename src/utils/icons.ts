/** Map CMS emoji icons to SVG icon names used by Icon.astro */
export const emojiToIcon: Record<string, string> = {
  '🔧': 'wrench',
  '⚡': 'bolt',
  '💅': 'sparkles',
  '💇': 'sparkles',
  '💈': 'sparkles',
  '🎨': 'paintbrush',
  '🪚': 'hammer',
  '🧹': 'broom',
  '❄️': 'snowflake',
  '🔌': 'bolt',
  '🧱': 'hammer',
  '🐛': 'shield-check',
  '👔': 'sparkles',
  '🌿': 'home',
  '🛋️': 'home',
  '🤖': 'cpu',
  '🏠': 'home',
  '🎯': 'target',
  '⭐': 'star-badge',
  '✅': 'shield-check',
  '💬': 'message',
};

export function iconNameFromEmoji(emoji?: string, fallback = 'wrench'): string {
  if (!emoji) return fallback;
  return emojiToIcon[emoji] ?? fallback;
}
