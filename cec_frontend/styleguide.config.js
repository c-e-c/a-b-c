const path = require('path')

function resolve(dir) {
  return path.join(__dirname, '..', dir)
}

module.exports = {
  //components: 'src/components/**/[A-Z]*.vue',
  components: function () {
    return [
      'src/components/Widgets/SimpleTable.vue',
      'src/components/Widgets/SimplePagination.vue',
    ]
  },

  // sections: [{
  //   name: 'Form',
  //   // content: 'docs/SimpleForm.md',
  //   components: function () {
  //     return [
  //       'src/components/Widgets/SimpleForm.vue',
  //       // 'src/components/Form/DynamicEditor.vue',
  //     ]
  //   }
  // }, {
  //   name: 'Filter',
  //   // content: 'docs/SimpleForm.md',
  //   components: function () {
  //     return [
  //       'src/components/Widgets/SimpleFilter.vue',
  //     ]
  //   }
  // }
  // ],

  webpackConfig: require('./build/webpack.base.conf.js'),

  showUsage: true,
  highlightTheme: 'dracula',

  theme: {
    color: {
      link: 'firebrick',
      linkHover: 'salmon',
    },
    // fontFamily: {
    //   base: '"Comic Sans MS", "Comic Sans", cursive'
    // }
  },
  styles: {
    Logo: {
      // logo: {
      //   animation: 'blink ease-in-out 300ms infinite'
      // },
      '@keyframes blink': {
        to: {
          opacity: 0
        }
      }
    }
  }

  // webpackConfig: {
  //     module: {
  //       rules: [
  //         // Vue loader
  //         {
  //           test: /\.vue$/,
  //           exclude: /node_modules/,
  //           loader: 'vue-loader'
  //         },
  //         // Babel loader, will use your project’s .babelrc
  //         {
  //           test: /\.js?$/,
  //           exclude: /node_modules/,
  //           loader: 'babel-loader'
  //         },
  //         // Other loaders that are needed for your components
  //         {
  //           test: /\.css$/,
  //           loader: 'style-loader!css-loader'
  //         }
  //       ]
  //     }
  //   }

  //   defaultExample: true,
  //   webpackConfig: {
  //       module: {
  //           loaders,
  //       },
  //   },
  //   showUsage: true,
  //   serverPort: 6062,
  //   vuex: 'src/store/index.js',
}
