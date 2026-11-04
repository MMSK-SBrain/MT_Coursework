/** @type {import('next').NextConfig} */
const nextConfig = {
  // Workspace packages (@cg/core, later @cg/harness and @cg/exports) ship TypeScript source.
  transpilePackages: ["@cg/core"],
  eslint: { ignoreDuringBuilds: true },
  serverExternalPackages: ["postgres"],
  webpack(config) {
    // Workspace packages import "./model.js" that is really model.ts.
    config.resolve.extensionAlias = { ".js": [".ts", ".tsx", ".js"] };
    return config;
  },
};
export default nextConfig;
