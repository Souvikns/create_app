import os


class output:
    def __init__(self):
        self.name = ""
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
        with open("../react.json") as f:
            with open("package.json", "w") as f1:
                for line in f:
                    f1.write(line)
        os.mkdir("public")
        os.chdir("./public")
        os.system("type nul > index.html")
        with open("../../index.html") as f:
            with open("index.html", "w") as f1:
                for line in f:
                    f1.write(line)
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
