const { defineConfig } = require('@vue/cli-service')
const webpack = require('webpack')
module.exports = defineConfig({
  transpileDependencies: true,
  // lintOnSave:false, //关闭哦语法检查
  // devServer: {
  //   // host: '0.0.0.0',
  //   // // https:true,
  //   // port: 8080,
  //   // client: {
  //   //   webSocketURL: '0.0.0.0:8080',
  //   // },
  //   // headers: {
  //   //   'Access-Control-Allow-Origin': '*',
  //   // }
  // }, 
})

 
// configureWebpack: {

//     plugins: [
//         new webpack.ProvidePlugin({
//         $: 'jquery',
//         jQuery: 'jquery',
//         'windows.jQuery': 'jquery'
//         })
//     ]
// }
