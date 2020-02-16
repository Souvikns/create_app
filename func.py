import os


class output:
    def __init__(self):
        self.name = ""
        self.pckjson = '''{
  "name": "react-template",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^4.2.4",
    "@testing-library/react": "^9.4.0",
    "@testing-library/user-event": "^7.2.1",
    "react": "^16.12.0",
    "react-dom": "^16.12.0",
    "react-scripts": "3.3.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": "react-app"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
        '''
        self.indxht = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>

        '''
        self.appjs = '''import React from 'react';

function App() {
  return (
    <div>

    </div>
  );
}

export default App;
'''
        self.indexjs = '''import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));

'''

    def createReactApp(self, x):
        self.name = x
        os.mkdir(x)
        path = './' + x
        os.chdir(path)
        os.system("type nul > package.json")
        os.system("type nul > .gitignore")
        file = open("package.json", "w")
        file.write(self.pckjson)
        file.close()
        # with open("../react.json") as f:
        #     with open("package.json", "w") as f1:
        #         for line in f:
        #             f1.write(line)
        os.mkdir("public")
        os.chdir("./public")
        os.system("type nul > index.html")
        file = open("index.html", "w")
        file.write(self.indxht)
        file.close()
        os.chdir("../")
        os.mkdir("src")
        os.chdir("./src")
        os.system("type nul > App.js")
        file = open("App.js","w")
        file.write(self.appjs)
        file.close()
        os.system("type nul > index.js")
        file = open("index.js", "w")
        file.write(self.indexjs)
        file.close()
        os.system("npm install")
        output_react = f'''React app created\ncd over to {self.name}'''
        print(output_react)

    def createExpressApp(self, x):
        self.name = x
        os.mkdir(x)
        path = './' + x
        os.chdir(path)
        os.system("npm init -y")
        os.system("type nul > app.js")
        os.system("type nul > .gitignore")
        os.system("npm i express body-parser")
        output_express = f'''Express app created\ncd over to {self.name}'''
        print(output_express)
