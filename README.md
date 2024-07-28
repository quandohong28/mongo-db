## MongoDB

- I have compiled MongoDB and MongoDB Compass versions for MacOS. You can download and install them according to the following instructions.

- Official Link:

    + [MongoDB Comunity Server](https://www.mongodb.com/try/download/community)
    + [MongoDB Compass (GUI))](https://www.mongodb.com/try/download/compass)
    + [MongoDB Shell](https://www.mongodb.com/try/download/shell)


## Requirements

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
## How to install

#### Step 1: Download the file that matches your configuration.

#### Step 2: Install MongoDB Compass first.

#### Step 3: Open and extract the downloaded file.

#### Step 4: Create a new folder named `mongodb`

```
    $ sudo mkdir -p /usr/local/bin/mongodb

    $ sudo chmod -R 777 /usr/local/bin/mongodb
```

#### Step 5: Move the extracted files to the `mongodb` folder.

```
    $ sudo mv ~/Downloads/folder-extracted/bin /usr/local/bin/mongodb
```

#### Step 6: Set mongodb as environment variable

- If you are using zsh
```
    $ echo 'export PATH=/usr/local/bin/mongodb/bin:$PATH' >> ~/.zshrc

    $ source ~/.zshrc
```

- If you are using bash

```
    $ echo 'export PATH=/usr/local/bin/mongodb/bin:$PATH' >> ~/.bash_profile

    $ source ~/.bash_profile
```

#### Step 7: Make folder to save data

```
    $ sudo mkdir -p /usr/local/bin/mongodb/data/db

    $ sudo chown -R $(whoami):staff /usr/local/mongodb/data/db

    $ sudo chmod -R 775 /usr/local/mongodb/data/db
```

#### Step 8: Check the installation

```
    $ mongod --version

    $ mongo --version
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
