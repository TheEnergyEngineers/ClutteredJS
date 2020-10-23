# The Impact of Cluttered JavaScript Code in Mobile Web Apps with respect to Energy Consumption

This repository showcases the ClutteredJS experiment developed by the team **The Energy Engineers** for the Green Lab course at Vrije Universiteit Amsterdam for the academic year 2020-2021. All the information required to replicate the experiment is provided below.

## 1. Overview

Mobile phones are a major contributor to internet traffic around the world. Although the energy usage of a single smartphone may be considered modest, the overall energy footprint left by mobile devices is far higher. Concerning the energy consumption of different web elements in a mobile device, JavaScript is a major contributor. [JSCleaner](https://github.com/comnetsAD/MITM_JSCleaner) is a JavaScript decluttering tool for mobile web apps. In this experiment, we aim to analyze the impact of cluttered JavaScript code on the energy consumption.

## 2. Experiment Setup

The list of (cluttered and de-cluttered) mobile web apps that we used in the experiment is provided in the [Subject Selection Code](./Subject%20Selection%20Code) folder. The URLs are then [analyzed](./Subject%20Selection%20Code/subjectSelection.ipynb) for subject selection.

### 2.1 System Setup

- Elementary OS 5.1.6 (Linux Distro based on Ubuntu LTS 18.04)
- Android Device (Google Pixel 3 with Android v9.0.0)
- Android Studio (v4.1)
- Python v3.8.0
- Java Development Kit (JDK v8)
- R Studio (v1.3.1093)

### 2.2 Setup Architecture
<p align="center">
<img src="./docs/architecture.png" alt="Setup Architecture" width="400"/>
</p>

## 3. Experiment Execution

### 3.1 Android Runner

For the execution of the experiment, we used the [Android Runner](https://github.com/S2-group/android-runner) framework which allows automatic execution of measurement-based experiments on native and mobile web apps running on Android devices. All the experiment-specific Python scripts and configs are included in the [ClutteredJS/src](./ClutteredJS/src) folder.

### 3.2 MITM Proxy

The cluttered and decluttered web applications are hosted using [MITM Proxy](https://mitmproxy.org/) with separate ports for each kind. The mitm proxy certificate is installed in the android device after configuring it with appropriate IP address and port for the mitmproxy.


### 3.3 Execution and Output
```
python3 ClutteredJS ClutteredJS/src/config.json
```

The experiment can be executed using the above command and the corresponding output for the run will be stored in `ClutteredJS/src/output` folder.
The output of the experiments of the cluttered and de-cluttered mobile web apps are stored in the [ClutteredJS/src/output.nw](./ClutteredJS/src/output.nw) and [ClutteredJS/src/output.jsc](./ClutteredJS/src/output.jsc) folders respectively.

## 4. Results and Analysis

The output of the experiment is [analysed](./R%20Code), plotted, and tested using paired t-tests. Detailed analysis and results of the experiment are included in the [Report](./Report) folder.

## 5. Authors and Acknowledgments

The experiment is designed, developed, and executed by [Marc Wiggerman](mailto:m.g.wiggerman@student.vu.nl), [Sophie Vos](mailto:s.o.vos@student.vu.nl), [Geoffrey van Driessel](mailto:g.r.van.driessel@student.vu.nl), and [Abijith Radhakrishnan](mailto:mail@abijith.net). 
We thank [Dr. Ivano Malavolta](http://www.ivanomalavolta.com/) for his guidance and detailed feedback. We would also like to thank [JSCleaner research team](https://nyuscholars.nyu.edu/en/publications/jscleaner-de-cluttering-mobile-webpages-through-javascript-cleanu) for their research and providing access to the cluttered and de-cluttered mobile web pages though the MITM proxy server.
