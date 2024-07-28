## MongoDB

- I have compiled MongoDB, MongoDB Shell and MongoDB Compass versions for MacOS. You can download and install them according to the following instructions.
- MongoDB Control Panel is tool help you manage mongo server with button, so easy!

- Official Link:

    + [MongoDB Comunity Server](https://www.mongodb.com/try/download/community)
    + [MongoDB Compass (GUI))](https://www.mongodb.com/try/download/compass)
    + [MongoDB Shell](https://www.mongodb.com/try/download/shell)


## Requirements

- Mac ARM: MacOS 11 (Big Sur) or higher

- Mac Intel: MacOS 10.13 (High Sierra) or higher

`Check your system device info`
```
    $ neofetch
```

- Python3

```
    $ python3 --version
```

- Pip

```
    $ pip --version
```


#### Mongo (core)

- MacOS ARM64
    + [Mongod 6.0.16](https://fastdl.mongodb.org/osx/mongodb-macos-arm64-6.0.16.tgz): macOS 11.0 (Big Sur) or higher
    + [Mongod 7.0.12](https://fastdl.mongodb.org/osx/mongodb-macos-arm64-7.0.12.tgz): macOS 11.0 (Big Sur) or higher
    + [Mongod 8.0.0](https://fastdl.mongodb.org/osx/mongodb-macos-arm64-8.0.0-rc15.tgz): macOS 11.0 (Big Sur) or higher

- MacOS Intel
    + [Mongod 4.1.1](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.1.1.tgz): macOS 10.13 (High Sierra) or higher
    + [Mongod 5.0.28](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-5.0.28.tgz): macOS 10.15 (Catalina) or higher
    + [Mongod 6.0.16](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.16.tgz): macOS 11.0 (Big Sur) or higher
    + [Mongod 7.0.12](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-7.0.12.tgz): macOS 11.0 (Big Sur) or higher
    + [Mongod 8.0.0](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-8.0.0-rc15.tgz): macOS 11.0 (Big Sur) or higher

#### MongoDB Compass

- MacOS ARM64
    + [MongoDB Compass 1.43.4](https://downloads.mongodb.com/compass/mongodb-compass-1.43.4-darwin-arm64.dmg): macOS 11.0 (Big Sur) or higher

- MacOS Intel
    + [MongoDB Compass 1.27.0](https://downloads.mongodb.com/compass/mongodb-compass-1.27.0-darwin-x64.dmg): macOS 10.13 (High Sierra) or higher
    + [MongoDB Compass 1.32.0](https://downloads.mongodb.com/compass/mongodb-compass-1.32.0-darwin-x64.dmg): macOS 10.14 (Mojave) or higher
    + [MongoDB Compass 1.43.4](https://downloads.mongodb.com/compass/mongodb-compass-1.43.4-darwin-x64.dmg): macOS 10.15 (Catalina) or higher

#### MongoDB Shell

- MacOS ARM64
    + [MongoDB Shell 1.10.6](https://downloads.mongodb.com/compass/mongosh-1.10.6-darwin-arm64.zip): macOS 11.0 (Big Sur) or higher
    + [MongoDB Shell 2.2.12](https://downloads.mongodb.com/compass/mongosh-2.2.12-darwin-arm64.zip): macOS 11.0 (Big Sur) or higher

- MacOS Intel
    + [MongoDB Shell 1.10.6](https://downloads.mongodb.com/compass/mongosh-1.10.6-darwin-x64.zip): macOS 10.14 (Mojave) or higher
    + [MongoDB Shell 2.2.12](https://downloads.mongodb.com/compass/mongosh-2.2.12-darwin-x64.zip): macOS 11.0 (Big Sur) or higher


## How to install MongoDB core

#### Step 1: Download the file that matches your device OS version.

#### Step 2: Open and extract the downloaded file.

#### Step 3: Create a new folder named `mongodb`

```
    $ sudo mkdir -p /usr/local/mongodb

    $ sudo chmod -R 777 /usr/local/mongodb
```

#### Step 4: Move the extracted files to the `mongodb` folder.

```
    $ sudo mv ~/Downloads/folder-extracted/bin /usr/local/mongodb
```

#### Step 5: Set mongodb as environment variable

- If you are using zsh
```
    $ echo 'export PATH=/usr/local/mongodb/bin:$PATH' >> ~/.zshrc

    $ source ~/.zshrc
```

- If you are using bash

```
    $ echo 'export PATH=/usr/local/bin/mongodb/bin:$PATH' >> ~/.bash_profile

    $ source ~/.bash_profile
```

#### Step 6: Make folder to save data

```
    $ sudo mkdir -p /usr/local/bin/mongodb/data/db

    $ sudo chown -R $(whoami):staff /usr/local/mongodb/data/db

    $ sudo chmod -R 775 /usr/local/mongodb/data/db
```

#### Step 7: Check the installation

```
    $ mongod --version

    $ mongo --version
```


## How to install MongoDB Compass

#### Step 1: Download the file that matches your device OS version.

#### Step 2: Open and extract the downloaded file.

#### Step 3: Move the extracted file to the `Applications` folder.


## How to install MongoDB Shell
`using for mongodb version 6.0 or higher`

#### Step 1: Download the file that matches your device OS version.

#### Step 2: Open and extract the downloaded file.

#### Step 3: Move the extracted files to the `mongodb` folder.

```
    $ sudo mv ~/Downloads/folder-extracted/bin/mongosh /usr/local/mongodb/bin
```


## How to run

- Start MongoDB

```
    $ mongod --dbpath /usr/local/bin/mongodb/data/db
```

- Using MongoDB Shell

```
    $ mongo
```

or

```
    $ mongosh
```


## MongoDB GUI Control Panel

#### Step 1: Clone the repository

```
    $ git clone https://github.com/quandohong28/mongo-db.git
```

#### Step 2: Open the `mongo-db` folder

```
    $ cd mongo-db
```

#### Step 3: Install libs

```
    $ pip install tkinter threading subprocess pyinstaller
```

#### Step 4: Run the script

```
    $ python3 mongo-control-panel.py
```

#### Step 5: Build the app

```
    $ pyinstaller --onefile mongo-control-panel.py
```

#### Step 6: Set the app to the `mongodb/bin` folder to run it from anywhere

```
    $ mv dist/mongo-control-panel /usr/local/mongodb/bin
```

#### Step 7: Run the app

```
    $ mongo-control-panel
```
