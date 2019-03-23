const path=require('path')

module.exports = {
    outputDir: path.resolve(__dirname, '../server/dist'),
	// configureWebpack: {
	//     resolve: {
	//       alias: {
	//         "~": path.resolve(__dirname, 'node_modules/tone/build/')
	//       }
	//     }
	//   }
}