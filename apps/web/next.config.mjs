/** @type {import('next').NextConfig} */
const nextConfig = {
  // Workspace packages ship TypeScript source.
  transpilePackages: ["@cg/core", "@cg/harness", "@cg/exports"],
  eslint: { ignoreDuringBuilds: true },
  serverExternalPackages: ["postgres", "pptxgenjs", "docx", "mammoth", "unpdf", "exceljs"],
  webpack(config) {
    // Workspace packages import "./model.js" that is really model.ts.
    config.resolve.extensionAlias = { ".js": [".ts", ".tsx", ".js"] };
    return config;
  },
};
export default nextConfig;
