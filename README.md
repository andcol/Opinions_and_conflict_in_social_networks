# Opinions and conflict in social networks
Code for the Opinions and conflict in social networks exam, part of BISS 2022.
For further information, refer to the project report in the main exam document (Section 2.2).

## Configuring the environment
To execute the project, Python 3 and Virtualenv are required. To create the environment and install the necessary dependencies, from the main directory run:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

Next, to configure the network-disruption submodule run
```
git submodule init
git submodule update
```

## Running the visualization
The data and preprocessing tools necessary for the visualization are contained in the network-disruption submodule, and come from [Mayee F. Chen and Miklós Z. Rácz. Network disruption: maximizing disagreement and polarization in social networks](https://github.com/mayeechen/network-disruption). Twitter data needs pre-processing, refer to [this link](https://github.com/mayeechen/network-disruption/tree/master/preprocess-twitter) for instructions on how to compile and run the pre-processing utility.

To run the visualization of the Twitter and Reddit networks, from the main directory run
```
python twitter.py
python reddit.py
```
The resulting networks are shown in a separate Matplotlib window and can be navigated with the standard Matplotlib controls in the bottom left. The nodes are color-coded from red to blue according to their estimated innate opinions.
