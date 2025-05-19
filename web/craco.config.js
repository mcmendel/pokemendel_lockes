module.exports = {
  webpack: {
    configure: {
      resolve: {
        fallback: {
          // Add any polyfills if needed
        },
      },
      module: {
        rules: [
          {
            test: /\.m?js/,
            resolve: {
              fullySpecified: false
            }
          }
        ]
      }
    }
  }
}; 