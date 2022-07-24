# UniquenessDAO

UniquenessDAO is a voting mechanism which uses machine learning to assign each voter a uniqueness score.


<p align="center">•
  <a href="#setup">Setup</a> •
  <a href="#demo">Demo</a> •
  <a href="#team">Team</a> •
  <a href="#features">Features</a> •
  <a href="#vision">Vision</a> •
  <a href="#license">License</a> •
</p>

## Setup

### Prerequisites
Install node >= 14 and npm. Run the command:

```bash
$ npm install -g npm
```
to install the dependencies.

Proceed to the directory deploy, deploy.js for more information for setup.

## Demo
Walkthrough: https://www.youtube.com/watch?v=Tm6-Y1O-2es
## Team

### Zac
Email: zacyapjq@gmail.com <br/>
Github: https://github.com/zacyapjq <br/>

### YZ
Email: theheralding@gmail.com <br/>
Github: https://github.com/YZLoh <br/>

### George
Email: gkoumoussis@gmail.com <br/>
Github: https://github.com/gkoum-7 <br/>

### Riki
Email: gkoumoussis@gmail.com <br/>
Github: https://github.com/riki91 <br/>

### Wayne
Email: devchain7890@gmail.com <br/>
Github: https://github.com/hougangdev <br/>

## Features
- Uses machine learning to assign each voter a uniqueness score.
- Filecoin IPFS allows us to store the input data, intermediate ML model outputs and uniqueness scores assigned to each user for each DAO proposal vote with provable authenticity and Chainlink oracles external adapter allow us to read the data using a smart contract. (Watch <a href="#demo">Demo</a> for example. Here's the [contract](https://github.com/UniquenessDAO/SnapshotData/blob/master/contracts/getScoreREMIX_IDE.sol) and [CID](https://bafybeibhgwglemzhwhhxce3je3wyo4jksl7uu5hmttmwuvnyele6umkdhq.ipfs.dweb.link/testaddress.json) to json file on web3storage) <br/>
- Voter uniqueness is based on the type of proposal as determined by a Machine Learning clustering algorithm. Voter weights (also termed uniqueness scores) range from 0 to 100, and are calculated based on the voter’s composition of voting patterns.

## Vision

## License
The MIT License (MIT)
