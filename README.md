
  
# T-AIA-901-NAN_2
 
# Software Installation
This class is technically oriented.  A successful student needs to be able to compile and execute Python code that makes use of TensorFlow for deep learning. There are two options for you to accomplish this:

* Install Python, Spacy, Sklearn and some IDE (Jupyter, TensorFlow, and others)

## Installing Python and TensorFlow

It is possible to install and run Python/TensorFlow entirely from your computer.  Google provides TensorFlow for Windows, Mac, and Linux.  Previously, TensorFlow did not support Windows.  However, as of December 2016, TensorFlow supports Windows for both CPU and GPU operation.

The first step is to install Python 3.9.  This is the latest version of Python 3.  I recommend using the Miniconda (Anaconda) release of Python, as it already includes many of the data science related packages that are needed by this class.  Anaconda directly supports Windows, Mac, and Linux.  Miniconda is the minimal set of features from the extensive Anaconda Python distribution.  Download Miniconda from the following URL:

* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

# Python 3.9

*Note: I will remove this section once all needed libraries add support for Python 3.9.

**execute the following commands:** 

```
conda create -y --name nlp python=3.9
```

To enter this environment, you must use the following command (**for Windows**), this command must be done every time you open a new Anaconda/Miniconda terminal window:

```
activate nlp
```


For **Mac**, do this:

```
source activate nlp
```

# Installing Jupyter

it is easy to install Jupyter notebooks with the following command:

```
conda install -y jupyter
```

Once Jupyter is installed, it is started with the following command:

```
jupyter notebook
```

You should also link your new **tensorflow** environment to Jupyter so that you can choose it as a Kernal.  Always make sure to run your Jupyter notebooks from your 3.9 kernel.

```
python -m ipykernel install --user --name nlp --display-name "Python 3.9 (nlp)"
```
```
# What version of Python do you have?
import sys

import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
print("GPU is", "available" if tf.test.is_gpu_available() else "NOT AVAILABLE")
```

# Launch main project

To launch the project you have to install packages from the requirements.txt file.
To do so, go to the ui directory:

````
cd ui/
````

Next, install packages:

````
pip install -r requirements.txt
````

Install also french trained model from spacy:

````
python -m spacy download fr_core_news_lg
````

After that, you can launch the project properly:

````
python main.py
````

You can test each module in the notebooks folder at root.
Each module have its file:
- Extraction Location -> test_class_extraction_location.ipynb
- Search Path -> test_class_search_path.ipynb
- Vocal Recognition -> test_class_reco_vocal.ipynb
