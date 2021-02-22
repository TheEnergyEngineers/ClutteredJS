# The Impact of Cluttered JavaScript Code in Mobile Web Apps with respect to Energy Consumption

This repository showcases the ClutteredJS experiment developed by the team **The Energy Engineers** for the Green Lab course at Vrije Universiteit Amsterdam for the academic year 2020-2021. All the information required to replicate the experiment is provided below.

## 1. Overview

Mobile phones are a major contributor to internet traffic around the world. Although the energy usage of a single smartphone may be considered modest, the overall energy footprint left by mobile devices is far higher. Concerning the energy consumption of different web elements in a mobile device, JavaScript is a major contributor. [JSCleaner](https://github.com/comnetsAD/MITM_JSCleaner) is a JavaScript decluttering tool for mobile web apps. In this experiment, we aim to analyze the impact of cluttered JavaScript code on the energy consumption.

Note: Since our original experiments, we have modified the experiment setup to fix some of the threats to validity. Previously, the experiment will be run for a constant duration of 1 minute for every website. The revised experiment setup stops energy profiling immediately after the page load in the browser.

## 2. Experiment Setup

The list of (cluttered and de-cluttered) mobile web apps that we used in the experiment is provided in the [Subject Selection Code](./Subject%20Selection%20Code) folder. The URLs are then analyzed for subject selection (see [Subject Selection](./Subject%20Selection%20Code/subjectSelection.ipynb)).

### 2.1 System Setup

- Elementary OS 5.1.6 (Linux Distro based on Ubuntu LTS 18.04)
- Android Device (Huawei Nexus 6P)
- Android Studio (v4.1)
- Python v3.8.0
- Java Development Kit (JDK v8)
- R Studio (v1.3.1093)
- Google Chrome for Android (v88.0.4324.181)
- Android Debug Bridge version 1.0.39


### 2.2 Setup Architecture
<p align="center">
<img src="./docs/architecture.png" alt="Setup Architecture" width="400"/>
</p>

## 3. Experiment Execution

### 3.1 Android Runner

For the execution of the experiment, we used the [Android Runner](https://github.com/S2-group/android-runner) framework which allows automatic execution of measurement-based experiments on native and mobile web apps running on Android devices. All the experiment-specific Python scripts and configs are included in the [ClutteredJS/src](./ClutteredJS/src) folder.

### 3.2 MITM Proxy

The cluttered and de-cluttered mobile web apps are hosted using [MITM Proxy](https://mitmproxy.org/) with separate ports for each kind. The MITM proxy certificate is installed in the android device after configuring it with the appropriate IP address and port for the MITM proxy.

### 3.3 Setting Up Your Device

Identify your device ID by running `adb devices` in your terminal after enabling USB Debugging under Developer Options. Update the `devices.json` file with this ID and an appropriate name. This name will be used in the experiment config file (`config.json`) to identify the device.

### 3.4 Configuring Your Experiment

The experiment can be configured using the configuration file in ClutteredJS/src/config.json. The different websites to be profiled can be included inside the “paths” parameter. Furthermore, update the “devices”, “repetitions” and “time_between_run” parameters with appropriate values.

### 3.5 Updating HTML
Add the following script to the index.html of the websites you want to profile after updating the IP address with that of the computer on which the Android Runner framework will be run.

```
<script>
    function xml_http_post(url, data, callback) { 
        var req = new XMLHttpRequest();
        req.open("POST", url, true) ; 
        req.send(data);
    }
    function calcaulate_performance() {
        var plt = window.performance.timing.domComplete - window.performance.timing.requestStart;
        console.log("Calculated PLT: " + plt);
        xml_http_post("http://<COMPUTER_IP_ADDRESS>:8080/", { "plt" : plt }, null)
    }
    window.addEventListener ? window.addEventListener("load", calcaulate_performance, true) : window.attachEvent && window.attachEvent("onload", calcaulate_performance);
</script>
```

The experiments are observed by a web server which is automatically started when running the framework. This web server is notified when a web page is loaded on the android device (in Chrome) after which it notifies Android runner that it can stop profiling subject/website and that it can start aggregating the results. This web server thus limits the execution time of each experiment to the page load time instead of a fixed timer (which was used in the original experiments). 

### 3.3 Execution and Output
To perform the experiments the following command can be run:
```
python3 ClutteredJS ClutteredJS/src/config.json
```

The corresponding output for the run will be stored in `ClutteredJS/src/output` folder.

## 4. Results and Analysis

The output of the experiment is analyzed, plotted, and tested in R (see [R Code](./R%20Code)). Detailed analysis and results of the experiment are included in the [Report](./Report) folder.

## 5. Authors and Acknowledgments

The experiment is designed, developed, and executed by [Marc Wiggerman](mailto:m.g.wiggerman@student.vu.nl), [Sophie Vos](mailto:s.o.vos@student.vu.nl), [Geoffrey van Driessel](mailto:g.r.van.driessel@student.vu.nl), and [Abijith Radhakrishnan](mailto:mail@abijith.net). 
We thank [Dr. Ivano Malavolta](http://www.ivanomalavolta.com/) for his guidance and detailed feedback. We would also like to thank the [JSCleaner research team](https://nyuscholars.nyu.edu/en/publications/jscleaner-de-cluttering-mobile-webpages-through-javascript-cleanu) for their research and providing us with access to the cluttered and de-cluttered mobile web pages through the MITM proxy server.
