{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"center\" width=100%>\n",
    "    <tr>\n",
    "        <td width=\"15%\">\n",
    "            <img src=\"taxi.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"center\">\n",
    "                <font color=\"#21618C\" size=24px>\n",
    "                    <b>Taxi Fare Prediction\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Problem Statement\n",
    "\n",
    "This case study is to predict the taxi fare for a taxi ride in New York City from a given pickup point to the agreed dropoff location. Decision tree and Random Forest regressor is used for the fare prediction."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Definition\n",
    "\n",
    "**unique_id**: Unique identifier or key for each record in the dataset - (string)    \n",
    "\n",
    "**date_time_of_pickup**: time when the ride started - (timestamp)\n",
    "\n",
    "**longitude_of_pickup**: Longitude of the taxi ride pickup point - (float) - (Numerical) \n",
    " \n",
    "**latitude_of_pickup**: Latitude of the taxi ride pickup point - (float) - (Numerical)\n",
    "    \n",
    "**longitude__of_dropoff**: Longitude of the taxi ride dropoff point  - (float) - (Numerical)\n",
    "    \n",
    "**latitude_of_dropoff**: Latitude of the taxi ride dropoff point - (float) - (Numerical)\n",
    "    \n",
    "**no_of_passenger**: count of the passengers during the ride - (integer) - (Numerical)\n",
    "    \n",
    "**amount**: (target variable)dollar amount of the cost of the taxi ride\n",
    "   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Icon Legends\n",
    "<table>\n",
    "  <tr>\n",
    "    <th width=\"25%\"> <img src=\"infer.png\" style=\"width:25%;\"></th>\n",
    "    <th width=\"25%\"> <img src=\"alsoreadicon.png\" style=\"width:25%;\"></th>\n",
    "    <th width=\"25%\"> <img src=\"todo.png\" style=\"width:25%;\"></th>\n",
    "    <th width=\"25%\"> <img src=\"quicktip.png\" style=\"width:25%;\"></th>\n",
    "  </tr>\n",
    "  <tr>\n",
    "    <td><div align=\"center\" style=\"font-size:120%\">\n",
    "        <font color=\"#21618C\"><b>Inferences from Outcome</b></font></div>\n",
    "    </td>\n",
    "    <td><div align=\"center\" style=\"font-size:120%\">\n",
    "        <font color=\"#21618C\"><b>Additional Reads</b></font></div>\n",
    "    </td>\n",
    "    <td><div align=\"center\" style=\"font-size:120%\">\n",
    "        <font color=\"#21618C\"><b>Lets do it</b></font></div>\n",
    "    </td>\n",
    "    <td><div align=\"center\" style=\"font-size:120%\">\n",
    "        <font color=\"#21618C\"><b>Quick Tips</b></font></div>\n",
    "    </td>\n",
    "\n",
    "</tr>\n",
    "\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Table of Contents\n",
    "\n",
    "1. **[Import Libraries](#import_lib)**\n",
    "2. **[Set Options](#set_options)**\n",
    "3. **[Read Data](#Read_Data)**\n",
    "4. **[Prepare and Analyze the Data](#data_preparation)**\n",
    "    - 4.1 - [Understand the Data](#Data_Understanding)\n",
    "        - 4.1.1 - [Data Type](#Data_Types)\n",
    "        - 4.1.2 - [Feature Engineering](#Feature_Eng)\n",
    "        - 4.1.3 - [Summary Statistics](#Summary_Statistics)\n",
    "        - 4.1.4 - [Discover Outliers](#outlier)\n",
    "        - 4.1.5 - [Missing Values](#Missing_Values)\n",
    "        - 4.1.6 - [Correlation](#correlation)\n",
    "    - 4.2 - [Exploratory Data Analysis](#EDA)\n",
    "        - 4.2.1 - [Peak hours](#Peak)\n",
    "        - 4.2.2 - [Mean fare for each hour during weekdays and weekends](#Mean_Fare)\n",
    "        - 4.2.3 - [Distribution of key numerical variables](#Distribution)\n",
    "5. **[Random Forest](#Random_Forest)**\n",
    "    - 5.1 - [Random Forest Model](#RF_Model)\n",
    "    - 5.2 - [Random Forest with GridSearchCV ](#RF_CV)\n",
    "6. **[Conclusion and Interpretation](#conclusion)**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='import_lib'></a>\n",
    "# 1. Import Libraries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Let us import the required libraries and functions.</b> \n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:17.760178Z",
     "start_time": "2022-01-26T20:29:26.366209Z"
    }
   },
   "outputs": [],
   "source": [
    "# suppress warnings \n",
    "from warnings import filterwarnings\n",
    "filterwarnings('ignore')\n",
    "\n",
    "# 'Os' module provides functions for interacting with the operating system \n",
    "import os\n",
    "\n",
    "# 'Pandas' is used for data manipulation and analysis\n",
    "import pandas as pd \n",
    "\n",
    "# 'Numpy' is used for mathematical operations on large, multi-dimensional arrays and matrices\n",
    "import numpy as np\n",
    "\n",
    "# 'Matplotlib' is a data visualization library for 2D and 3D plots, built on numpy\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "\n",
    "# 'Seaborn' is based on matplotlib; used for plotting statistical graphics\n",
    "import seaborn as sns\n",
    "\n",
    "from math import radians, cos, sin, sqrt, asin\n",
    "\n",
    "# 'Scikit-learn' (sklearn) emphasizes various regression, classification and clustering algorithms\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import metrics\n",
    "from sklearn import preprocessing\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.ensemble import RandomForestRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:17.790998Z",
     "start_time": "2022-01-26T20:30:17.760178Z"
    }
   },
   "outputs": [],
   "source": [
    "# set the plot size using 'rcParams'\n",
    "# once the plot size is set using 'rcParams', it sets the size of all the forthcoming plots in the file\n",
    "# pass width and height in inches to 'figure.figsize' \n",
    "plt.rcParams['figure.figsize'] = [15,8]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='set_options'></a>\n",
    "# 2. Set Options"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Now we make necessary changes to :<br><br>\n",
    "1. Display complete dataframe<br>\n",
    "2. To set the decimal place of a numeric output to 6\n",
    "</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:17.904624Z",
     "start_time": "2022-01-26T20:30:17.790998Z"
    }
   },
   "outputs": [],
   "source": [
    "# display all columns of the dataframe\n",
    "pd.options.display.max_columns = None\n",
    "\n",
    "# display all rows of the dataframe\n",
    "pd.options.display.max_rows = 50 # None\n",
    "\n",
    "# returns an output value upto 6 decimals\n",
    "pd.options.display.float_format = '{:.6f}'.format "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Read_Data'></a>\n",
    "# 3. Read Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Read and display data to get insights from the data.\n",
    "                    </b> \n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:18.708599Z",
     "start_time": "2022-01-26T20:30:17.904624Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>unique_id</th>\n",
       "      <th>amount</th>\n",
       "      <th>date_time_of_pickup</th>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <th>no_of_passenger</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>26:21.0</td>\n",
       "      <td>4.500000</td>\n",
       "      <td>2009-06-15 17:26:21 UTC</td>\n",
       "      <td>-73.844311</td>\n",
       "      <td>40.721319</td>\n",
       "      <td>-73.841610</td>\n",
       "      <td>40.712278</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>52:16.0</td>\n",
       "      <td>16.900000</td>\n",
       "      <td>2010-01-05 16:52:16 UTC</td>\n",
       "      <td>-74.016048</td>\n",
       "      <td>40.711303</td>\n",
       "      <td>-73.979268</td>\n",
       "      <td>40.782004</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>35:00.0</td>\n",
       "      <td>5.700000</td>\n",
       "      <td>2011-08-18 00:35:00 UTC</td>\n",
       "      <td>-73.982738</td>\n",
       "      <td>40.761270</td>\n",
       "      <td>-73.991242</td>\n",
       "      <td>40.750562</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30:42.0</td>\n",
       "      <td>7.700000</td>\n",
       "      <td>2012-04-21 04:30:42 UTC</td>\n",
       "      <td>-73.987130</td>\n",
       "      <td>40.733143</td>\n",
       "      <td>-73.991567</td>\n",
       "      <td>40.758092</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>51:00.0</td>\n",
       "      <td>5.300000</td>\n",
       "      <td>2010-03-09 07:51:00 UTC</td>\n",
       "      <td>-73.968095</td>\n",
       "      <td>40.768008</td>\n",
       "      <td>-73.956655</td>\n",
       "      <td>40.783762</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  unique_id    amount      date_time_of_pickup  longitude_of_pickup  \\\n",
       "0   26:21.0  4.500000  2009-06-15 17:26:21 UTC           -73.844311   \n",
       "1   52:16.0 16.900000  2010-01-05 16:52:16 UTC           -74.016048   \n",
       "2   35:00.0  5.700000  2011-08-18 00:35:00 UTC           -73.982738   \n",
       "3   30:42.0  7.700000  2012-04-21 04:30:42 UTC           -73.987130   \n",
       "4   51:00.0  5.300000  2010-03-09 07:51:00 UTC           -73.968095   \n",
       "\n",
       "   latitude_of_pickup  longitude_of_dropoff  latitude_of_dropoff  \\\n",
       "0           40.721319            -73.841610            40.712278   \n",
       "1           40.711303            -73.979268            40.782004   \n",
       "2           40.761270            -73.991242            40.750562   \n",
       "3           40.733143            -73.991567            40.758092   \n",
       "4           40.768008            -73.956655            40.783762   \n",
       "\n",
       "   no_of_passenger  \n",
       "0                1  \n",
       "1                1  \n",
       "2                2  \n",
       "3                1  \n",
       "4                1  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# read csv file using pandas\n",
    "df_taxi = pd.read_csv('../Dataset/TaxiFare.csv')\n",
    "\n",
    "# display the top 5 rows of the dataframe\n",
    "df_taxi.head()\n",
    "\n",
    "# Note: To display more rows, example 10, use head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The column `unique_id` contains the unique identifier for each observation, which is redundant for further analysis. Thus, we drop this column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:18.914740Z",
     "start_time": "2022-01-26T20:30:18.712176Z"
    }
   },
   "outputs": [],
   "source": [
    "# drop the column 'Id' using drop()\n",
    "# 'axis = 1' drops the specified column\n",
    "df_taxi = df_taxi.drop('unique_id', axis = 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='data_preparation'></a>\n",
    "# 4. Prepare and Analyze the Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Data preparation is the process of cleaning and transforming raw data before building predictive models. <br><br>\n",
    "                        Here we will analyze and prepare data to perform regression techniques:<br>\n",
    "                        1. Check dimensions of the dataframe in terms of rows and columns <br>\n",
    "                        2. Check the data types. If not as per business context, change the data types  <br>\n",
    "                        3. Study Summary Statistics <br>\n",
    "                        4. Distribution of Variables<br>\n",
    "                        5. Analyze relationship between numeric variables <br>\n",
    "                        6. Check for missing values<br>\n",
    "                        7. Study correlation<br>\n",
    "                        8. Analyze relationship between numeric and categoric variables <br><br>\n",
    "                        Note: It is an art to explore data and one will need more and more practice to gain expertise in this area. </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Data_Understanding'></a>\n",
    "## 4.1 Understand the Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Let us now see the number of variables and observations in the data.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:19.008227Z",
     "start_time": "2022-01-26T20:30:18.918772Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(50000, 7)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 'shape' returns the dimensions of the data\n",
    "df_taxi.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see the dataframe has 7 columns and 50000 rows. It means there are 7 variables and 50000 observations."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Data_Types'></a>\n",
    "### 4.1.1 Data Type\n",
    "\n",
    "Data has a variety of data types. The main types stored in pandas dataframes are object, float, int64, bool and datetime64. In order to learn about each attribute, it is always good for us to know the data type of each column."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>In order to know whether the datatype aof each variable is correct, we do the following:<br><br>\n",
    "                        1. Check the data type <br>\n",
    "                        2. Change the incorrect data type <br>\n",
    "                        3. Recheck the data type after the conversion <br>\n",
    "                        4. Feature engineering <br>\n",
    "                        5. Drop the redundant variables <br>\n",
    "                       </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Check the data type.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:19.134518Z",
     "start_time": "2022-01-26T20:30:19.014212Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "amount                  float64\n",
       "date_time_of_pickup      object\n",
       "longitude_of_pickup     float64\n",
       "latitude_of_pickup      float64\n",
       "longitude_of_dropoff    float64\n",
       "latitude_of_dropoff     float64\n",
       "no_of_passenger           int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# use 'dtypes' to check the data type of each variable\n",
    "df_taxi.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align='left'>\n",
    "    <tr>\n",
    "        <td width='8%'>\n",
    "            <img src='infer.png'>\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align='left', style='font-size:120%'>\n",
    "                <font color='#21618C'>\n",
    "                    <b>From the above output, we see that the data type of 'date_time_of_pickup' is 'object '.<br>\n",
    "\n",
    "But according to data definition, 'date_time_of_pickup 'is a date time stamp variable, which is wrongly interpreted as 'object', so we will convert this variable data type to 'datetime'.</br></b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Change the incorrect data type.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:26.799697Z",
     "start_time": "2022-01-26T20:30:19.145453Z"
    }
   },
   "outputs": [],
   "source": [
    "# convert object to datetime using to_datetime method from pandas\n",
    "#if error is set to'coerce', then invalid parsing will be set as NaT.\n",
    "df_taxi.date_time_of_pickup = pd.to_datetime(df_taxi.date_time_of_pickup, errors='coerce')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**3. Recheck the data type after the conversion.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:26.819804Z",
     "start_time": "2022-01-26T20:30:26.803429Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "amount                              float64\n",
       "date_time_of_pickup     datetime64[ns, UTC]\n",
       "longitude_of_pickup                 float64\n",
       "latitude_of_pickup                  float64\n",
       "longitude_of_dropoff                float64\n",
       "latitude_of_dropoff                 float64\n",
       "no_of_passenger                       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# recheck the data type of each column\n",
    "df_taxi.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "           <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Now the data type of each variable is as per the data definition.</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Feature_Eng'></a>\n",
    "### 4.1.2 Feature Engineering\n",
    "\n",
    "We will extract date time features from the variable 'date_time_of_pickup'."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>For feature engineering, we do the following:<br><br>\n",
    "                        1. Feature addition <br>\n",
    "                        2. Drop the redundant variables <br>\n",
    "                       </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Add new variables**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will extract new features from variable `date_time_of_pickup` . We will also add a variable which measures the distance between the pickup and dropoff point."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:27.275829Z",
     "start_time": "2022-01-26T20:30:26.823794Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>amount</th>\n",
       "      <th>date_time_of_pickup</th>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <th>no_of_passenger</th>\n",
       "      <th>hour</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>dayofweek</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>2009-06-15 17:26:21+00:00</td>\n",
       "      <td>-73.844311</td>\n",
       "      <td>40.721319</td>\n",
       "      <td>-73.841610</td>\n",
       "      <td>40.712278</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>15</td>\n",
       "      <td>6</td>\n",
       "      <td>2009</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>16.900000</td>\n",
       "      <td>2010-01-05 16:52:16+00:00</td>\n",
       "      <td>-74.016048</td>\n",
       "      <td>40.711303</td>\n",
       "      <td>-73.979268</td>\n",
       "      <td>40.782004</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2010</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5.700000</td>\n",
       "      <td>2011-08-18 00:35:00+00:00</td>\n",
       "      <td>-73.982738</td>\n",
       "      <td>40.761270</td>\n",
       "      <td>-73.991242</td>\n",
       "      <td>40.750562</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>18</td>\n",
       "      <td>8</td>\n",
       "      <td>2011</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7.700000</td>\n",
       "      <td>2012-04-21 04:30:42+00:00</td>\n",
       "      <td>-73.987130</td>\n",
       "      <td>40.733143</td>\n",
       "      <td>-73.991567</td>\n",
       "      <td>40.758092</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>21</td>\n",
       "      <td>4</td>\n",
       "      <td>2012</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.300000</td>\n",
       "      <td>2010-03-09 07:51:00+00:00</td>\n",
       "      <td>-73.968095</td>\n",
       "      <td>40.768008</td>\n",
       "      <td>-73.956655</td>\n",
       "      <td>40.783762</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>2010</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49995</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>2013-06-12 23:25:15+00:00</td>\n",
       "      <td>-73.999973</td>\n",
       "      <td>40.748531</td>\n",
       "      <td>-74.016899</td>\n",
       "      <td>40.705993</td>\n",
       "      <td>1</td>\n",
       "      <td>23</td>\n",
       "      <td>12</td>\n",
       "      <td>6</td>\n",
       "      <td>2013</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49996</th>\n",
       "      <td>7.500000</td>\n",
       "      <td>2015-06-22 17:19:18+00:00</td>\n",
       "      <td>-73.984756</td>\n",
       "      <td>40.768211</td>\n",
       "      <td>-73.987366</td>\n",
       "      <td>40.760597</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>22</td>\n",
       "      <td>6</td>\n",
       "      <td>2015</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49997</th>\n",
       "      <td>6.900000</td>\n",
       "      <td>2011-01-30 04:53:00+00:00</td>\n",
       "      <td>-74.002698</td>\n",
       "      <td>40.739428</td>\n",
       "      <td>-73.998108</td>\n",
       "      <td>40.759483</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>30</td>\n",
       "      <td>1</td>\n",
       "      <td>2011</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49998</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>2012-11-06 07:09:00+00:00</td>\n",
       "      <td>-73.946062</td>\n",
       "      <td>40.777567</td>\n",
       "      <td>-73.953450</td>\n",
       "      <td>40.779687</td>\n",
       "      <td>2</td>\n",
       "      <td>7</td>\n",
       "      <td>6</td>\n",
       "      <td>11</td>\n",
       "      <td>2012</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49999</th>\n",
       "      <td>10.900000</td>\n",
       "      <td>2010-01-13 08:13:14+00:00</td>\n",
       "      <td>-73.932603</td>\n",
       "      <td>40.763805</td>\n",
       "      <td>-73.932603</td>\n",
       "      <td>40.763805</td>\n",
       "      <td>1</td>\n",
       "      <td>8</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>2010</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>50000 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         amount       date_time_of_pickup  longitude_of_pickup  \\\n",
       "0      4.500000 2009-06-15 17:26:21+00:00           -73.844311   \n",
       "1     16.900000 2010-01-05 16:52:16+00:00           -74.016048   \n",
       "2      5.700000 2011-08-18 00:35:00+00:00           -73.982738   \n",
       "3      7.700000 2012-04-21 04:30:42+00:00           -73.987130   \n",
       "4      5.300000 2010-03-09 07:51:00+00:00           -73.968095   \n",
       "...         ...                       ...                  ...   \n",
       "49995 15.000000 2013-06-12 23:25:15+00:00           -73.999973   \n",
       "49996  7.500000 2015-06-22 17:19:18+00:00           -73.984756   \n",
       "49997  6.900000 2011-01-30 04:53:00+00:00           -74.002698   \n",
       "49998  4.500000 2012-11-06 07:09:00+00:00           -73.946062   \n",
       "49999 10.900000 2010-01-13 08:13:14+00:00           -73.932603   \n",
       "\n",
       "       latitude_of_pickup  longitude_of_dropoff  latitude_of_dropoff  \\\n",
       "0               40.721319            -73.841610            40.712278   \n",
       "1               40.711303            -73.979268            40.782004   \n",
       "2               40.761270            -73.991242            40.750562   \n",
       "3               40.733143            -73.991567            40.758092   \n",
       "4               40.768008            -73.956655            40.783762   \n",
       "...                   ...                   ...                  ...   \n",
       "49995           40.748531            -74.016899            40.705993   \n",
       "49996           40.768211            -73.987366            40.760597   \n",
       "49997           40.739428            -73.998108            40.759483   \n",
       "49998           40.777567            -73.953450            40.779687   \n",
       "49999           40.763805            -73.932603            40.763805   \n",
       "\n",
       "       no_of_passenger  hour  day  month  year  dayofweek  \n",
       "0                    1    17   15      6  2009          0  \n",
       "1                    1    16    5      1  2010          1  \n",
       "2                    2     0   18      8  2011          3  \n",
       "3                    1     4   21      4  2012          5  \n",
       "4                    1     7    9      3  2010          1  \n",
       "...                ...   ...  ...    ...   ...        ...  \n",
       "49995                1    23   12      6  2013          2  \n",
       "49996                1    17   22      6  2015          0  \n",
       "49997                1     4   30      1  2011          6  \n",
       "49998                2     7    6     11  2012          1  \n",
       "49999                1     8   13      1  2010          2  \n",
       "\n",
       "[50000 rows x 12 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# extract various date time components as seperate variables\n",
    "df_taxi = df_taxi.assign(hour = df_taxi.date_time_of_pickup.dt.hour, \n",
    "                         day = df_taxi.date_time_of_pickup.dt.day,\n",
    "                        month = df_taxi.date_time_of_pickup.dt.month, \n",
    "                        year = df_taxi.date_time_of_pickup.dt.year, \n",
    "                        dayofweek = df_taxi.date_time_of_pickup.dt.dayofweek)\n",
    "df_taxi"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will add a new variable which measures the distance between the pickup and dropoff point. We will use the Haversine formula to compute the distance between two points of the journey, using the logitude and latitude values. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"alsoreadicon.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>I love to know more:  </b><a href=\"https://en.wikipedia.org/wiki/Haversine_formula\"> What is Haversine </a>\n",
    "</font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:27.305540Z",
     "start_time": "2022-01-26T20:30:27.278784Z"
    }
   },
   "outputs": [],
   "source": [
    "# function to calculate the travel distance from the longitudes and latitudes\n",
    "def distance_transform(longitude1, latitude1, longitude2, latitude2):\n",
    "    travel_dist = []\n",
    "    \n",
    "    for pos in range(len(longitude1)):\n",
    "        long1,lati1,long2,lati2 = map(radians,[longitude1[pos],latitude1[pos],longitude2[pos],latitude2[pos]])\n",
    "        dist_long = long2 - long1\n",
    "        dist_lati = lati2 - lati1\n",
    "        a = sin(dist_lati/2)**2 + cos(lati1) * cos(lati2) * sin(dist_long/2)**2\n",
    "        c = 2 * asin(sqrt(a))*6371\n",
    "        travel_dist.append(c)\n",
    "       \n",
    "    return travel_dist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:27.421831Z",
     "start_time": "2022-01-26T20:30:27.305540Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.distance_transform(longitude1, latitude1, longitude2, latitude2)>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "distance_transform"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:27.726568Z",
     "start_time": "2022-01-26T20:30:27.429499Z"
    }
   },
   "outputs": [],
   "source": [
    "#Add a new variable travel distance\n",
    "\n",
    "df_taxi['travel_dist_km'] = distance_transform(df_taxi['longitude_of_pickup'].to_numpy(),\n",
    "                                                df_taxi['latitude_of_pickup'].to_numpy(),\n",
    "                                                df_taxi['longitude_of_dropoff'].to_numpy(),\n",
    "                                                df_taxi['latitude_of_dropoff'].to_numpy()\n",
    "                                              )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:27.747553Z",
     "start_time": "2022-01-26T20:30:27.726568Z"
    },
    "scrolled": 
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>amount</th>\n",
       "      <th>date_time_of_pickup</th>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <th>no_of_passenger</th>\n",
       "      <th>hour</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>dayofweek</th>\n",
       "      <th>travel_dist_km</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.500000</td>\n",
       "      <td>2009-06-15 17:26:21+00:00</td>\n",
       "      <td>-73.844311</td>\n",
       "      <td>40.721319</td>\n",
       "      <td>-73.841610</td>\n",
       "      <td>40.712278</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>15</td>\n",
       "      <td>6</td>\n",
       "      <td>2009</td>\n",
       "      <td>0</td>\n",
       "      <td>1.030764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>16.900000</td>\n",
       "      <td>2010-01-05 16:52:16+00:00</td>\n",
       "      <td>-74.016048</td>\n",
       "      <td>40.711303</td>\n",
       "      <td>-73.979268</td>\n",
       "      <td>40.782004</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2010</td>\n",
       "      <td>1</td>\n",
       "      <td>8.450134</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5.700000</td>\n",
       "      <td>2011-08-18 00:35:00+00:00</td>\n",
       "      <td>-73.982738</td>\n",
       "      <td>40.761270</td>\n",
       "      <td>-73.991242</td>\n",
       "      <td>40.750562</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>18</td>\n",
       "      <td>8</td>\n",
       "      <td>2011</td>\n",
       "      <td>3</td>\n",
       "      <td>1.389525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7.700000</td>\n",
       "      <td>2012-04-21 04:30:42+00:00</td>\n",
       "      <td>-73.987130</td>\n",
       "      <td>40.733143</td>\n",
       "      <td>-73.991567</td>\n",
       "      <td>40.758092</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>21</td>\n",
       "      <td>4</td>\n",
       "      <td>2012</td>\n",
       "      <td>5</td>\n",
       "      <td>2.799270</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.300000</td>\n",
       "      <td>2010-03-09 07:51:00+00:00</td>\n",
       "      <td>-73.968095</td>\n",
       "      <td>40.768008</td>\n",
       "      <td>-73.956655</td>\n",
       "      <td>40.783762</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>2010</td>\n",
       "      <td>1</td>\n",
       "      <td>1.999157</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     amount       date_time_of_pickup  longitude_of_pickup  \\\n",
       "0  4.500000 2009-06-15 17:26:21+00:00           -73.844311   \n",
       "1 16.900000 2010-01-05 16:52:16+00:00           -74.016048   \n",
       "2  5.700000 2011-08-18 00:35:00+00:00           -73.982738   \n",
       "3  7.700000 2012-04-21 04:30:42+00:00           -73.987130   \n",
       "4  5.300000 2010-03-09 07:51:00+00:00           -73.968095   \n",
       "\n",
       "   latitude_of_pickup  longitude_of_dropoff  latitude_of_dropoff  \\\n",
       "0           40.721319            -73.841610            40.712278   \n",
       "1           40.711303            -73.979268            40.782004   \n",
       "2           40.761270            -73.991242            40.750562   \n",
       "3           40.733143            -73.991567            40.758092   \n",
       "4           40.768008            -73.956655            40.783762   \n",
       "\n",
       "   no_of_passenger  hour  day  month  year  dayofweek  travel_dist_km  \n",
       "0                1    17   15      6  2009          0        1.030764  \n",
       "1                1    16    5      1  2010          1        8.450134  \n",
       "2                2     0   18      8  2011          3        1.389525  \n",
       "3                1     4   21      4  2012          5        2.799270  \n",
       "4                1     7    9      3  2010          1        1.999157  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Check the newly added vaiarbles\n",
    "df_taxi.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Drop the redundant variable.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we have extracted new features from variable `date_time_of_pickup` this variable is redundant for further analysis. Hence we drop this variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:27.910723Z",
     "start_time": "2022-01-26T20:30:27.749550Z"
    }
   },
   "outputs": [],
   "source": [
    "# drop the column 'date_time_of_pickup' using drop()\n",
    "# 'axis = 1' drops the specified column\n",
    "\n",
    "df_taxi = df_taxi.drop('date_time_of_pickup',axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:28.456198Z",
     "start_time": "2022-01-26T20:30:27.910723Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 50000 entries, 0 to 49999\n",
      "Data columns (total 12 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   amount                50000 non-null  float64\n",
      " 1   longitude_of_pickup   50000 non-null  float64\n",
      " 2   latitude_of_pickup    50000 non-null  float64\n",
      " 3   longitude_of_dropoff  50000 non-null  float64\n",
      " 4   latitude_of_dropoff   50000 non-null  float64\n",
      " 5   no_of_passenger       50000 non-null  int64  \n",
      " 6   hour                  50000 non-null  int64  \n",
      " 7   day                   50000 non-null  int64  \n",
      " 8   month                 50000 non-null  int64  \n",
      " 9   year                  50000 non-null  int64  \n",
      " 10  dayofweek             50000 non-null  int64  \n",
      " 11  travel_dist_km        50000 non-null  float64\n",
      "dtypes: float64(6), int64(6)\n",
      "memory usage: 4.6 MB\n"
     ]
    }
   ],
   "source": [
    "df_taxi.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As now have the required features, after having extracted new ones and dropping the redundant variables."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Summary_Statistics'></a>\n",
    "### 4.1.3 Summary Statistics\n",
    "\n",
    "Here we take a look at the summary of each attribute. This includes the count, mean, the minimum and maximum values as well as some percentiles for numeric variables and count, unique, top, frequency for other variable types."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> In our dataset we have both numerical and categorical variables. Now we check for summary statistics of all the variables<br><br>\n",
    "                        1. For numerical variables, use the describe()<br>\n",
    "                        2. For categorical variables use the describe(include='object')\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. For numerical variables, use the describe()**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:28.693098Z",
     "start_time": "2022-01-26T20:30:28.456198Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>amount</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>11.364171</td>\n",
       "      <td>9.685557</td>\n",
       "      <td>-5.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>8.500000</td>\n",
       "      <td>12.500000</td>\n",
       "      <td>200.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>-72.509756</td>\n",
       "      <td>10.393860</td>\n",
       "      <td>-75.423848</td>\n",
       "      <td>-73.992062</td>\n",
       "      <td>-73.981840</td>\n",
       "      <td>-73.967148</td>\n",
       "      <td>40.783472</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>39.933759</td>\n",
       "      <td>6.224857</td>\n",
       "      <td>-74.006893</td>\n",
       "      <td>40.734880</td>\n",
       "      <td>40.752678</td>\n",
       "      <td>40.767360</td>\n",
       "      <td>401.083332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>-72.504616</td>\n",
       "      <td>10.407570</td>\n",
       "      <td>-84.654241</td>\n",
       "      <td>-73.991152</td>\n",
       "      <td>-73.980082</td>\n",
       "      <td>-73.963584</td>\n",
       "      <td>40.851027</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>39.926251</td>\n",
       "      <td>6.014737</td>\n",
       "      <td>-74.006377</td>\n",
       "      <td>40.734372</td>\n",
       "      <td>40.753372</td>\n",
       "      <td>40.768167</td>\n",
       "      <td>43.415190</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no_of_passenger</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>1.667840</td>\n",
       "      <td>1.289195</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hour</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>13.489080</td>\n",
       "      <td>6.506935</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>23.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>day</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>15.672040</td>\n",
       "      <td>8.660789</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>month</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>6.273300</td>\n",
       "      <td>3.461157</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>12.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>2011.739260</td>\n",
       "      <td>1.862639</td>\n",
       "      <td>2009.000000</td>\n",
       "      <td>2010.000000</td>\n",
       "      <td>2012.000000</td>\n",
       "      <td>2013.000000</td>\n",
       "      <td>2015.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dayofweek</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>3.029980</td>\n",
       "      <td>1.956936</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>travel_dist_km</th>\n",
       "      <td>50000.000000</td>\n",
       "      <td>18.508946</td>\n",
       "      <td>355.564309</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.223146</td>\n",
       "      <td>2.120114</td>\n",
       "      <td>3.895570</td>\n",
       "      <td>8667.818812</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            count        mean        std         min  \\\n",
       "amount               50000.000000   11.364171   9.685557   -5.000000   \n",
       "longitude_of_pickup  50000.000000  -72.509756  10.393860  -75.423848   \n",
       "latitude_of_pickup   50000.000000   39.933759   6.224857  -74.006893   \n",
       "longitude_of_dropoff 50000.000000  -72.504616  10.407570  -84.654241   \n",
       "latitude_of_dropoff  50000.000000   39.926251   6.014737  -74.006377   \n",
       "no_of_passenger      50000.000000    1.667840   1.289195    0.000000   \n",
       "hour                 50000.000000   13.489080   6.506935    0.000000   \n",
       "day                  50000.000000   15.672040   8.660789    1.000000   \n",
       "month                50000.000000    6.273300   3.461157    1.000000   \n",
       "year                 50000.000000 2011.739260   1.862639 2009.000000   \n",
       "dayofweek            50000.000000    3.029980   1.956936    0.000000   \n",
       "travel_dist_km       50000.000000   18.508946 355.564309    0.000000   \n",
       "\n",
       "                             25%         50%         75%         max  \n",
       "amount                  6.000000    8.500000   12.500000  200.000000  \n",
       "longitude_of_pickup   -73.992062  -73.981840  -73.967148   40.783472  \n",
       "latitude_of_pickup     40.734880   40.752678   40.767360  401.083332  \n",
       "longitude_of_dropoff  -73.991152  -73.980082  -73.963584   40.851027  \n",
       "latitude_of_dropoff    40.734372   40.753372   40.768167   43.415190  \n",
       "no_of_passenger         1.000000    1.000000    2.000000    6.000000  \n",
       "hour                    9.000000   14.000000   19.000000   23.000000  \n",
       "day                     8.000000   16.000000   23.000000   31.000000  \n",
       "month                   3.000000    6.000000    9.000000   12.000000  \n",
       "year                 2010.000000 2012.000000 2013.000000 2015.000000  \n",
       "dayofweek               1.000000    3.000000    5.000000    6.000000  \n",
       "travel_dist_km          1.223146    2.120114    3.895570 8667.818812  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# the describe() returns the statistical summary of the variables\n",
    "# by default, it returns the summary of numerical variables\n",
    "# use .transpose() for better readability. However it is optional\n",
    "df_taxi.describe().transpose()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "<b>The above output illustrates the summary statistics of all the numeric variables like mean, median (50%), standard deviation, minimum, and maximum values, along with the first and third quantiles.<br><br> \n",
    " <br><br>Note that the minimum amount is -5 and maximum is 200. Ideally fare amount should not be less that 2.5 dollars, which is the minimum value set for fares in NYC. Also the minimum count of passengers is 0, which isn't a practical scenario. We will deal with such values as we progress the case study.\n",
    "    </b>     </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. For categorical variables, use the describe(include='object').**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As, there are no categorical varaibles, we skip this step."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='outlier'></a>\n",
    "### 4.1.4 Discover Outliers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "rv_JBRXxeboi"
   },
   "source": [
    "#### Importance of detecting an outlier\n",
    "An outlier is an observation that appears to deviate distinctly from other observations in the data. If the outliers are not removed, the model accuracy may decrease.\n",
    "Let us detect the extreme values in the data. \n",
    "\n",
    "\n",
    "The following can be considered as outliers in this case study:\n",
    "1. Amount < 2.5\n",
    "2. Trips with travel distance less than or equal to 0, and more than 130Kms\n",
    "3. Trips where 90< latitude <-90, 180 < longitude < -180                     "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. We have seen that there are instances of amount less that 0 as well in the data set, where as the minimum fare for any trip in NYC is 2.5 dollars, hence we will remove such observations. We have already seen that the max fare is 200 in the data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.084016Z",
     "start_time": "2022-01-26T20:30:28.695092Z"
    }
   },
   "outputs": [],
   "source": [
    "#We will only keep the observation where fare is between 2.5\n",
    "df_taxi = df_taxi.loc[(df_taxi.amount >= 2.5)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.098942Z",
     "start_time": "2022-01-26T20:30:29.087968Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Remaining observastions in the dataset: (49990, 12)\n"
     ]
    }
   ],
   "source": [
    "print(\"Remaining observastions in the dataset:\", df_taxi.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Remove the observations with travel distance more than 130 kms.As seen from descriptive stats there are obs with travel distance more than 130 km, as that is the limit for trips in and around NYC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.286395Z",
     "start_time": "2022-01-26T20:30:29.102929Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Remaining observastions in the dataset: (49990, 12)\n"
     ]
    }
   ],
   "source": [
    "#We will only keep the observation where travel distance is less than or equal to 130\n",
    "\n",
    "df_taxi = df_taxi.loc[(df_taxi.travel_dist_km >= 1) | (df_taxi.travel_dist_km <= 130)]\n",
    "print(\"Remaining observastions in the dataset:\", df_taxi.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Remove the observations with unreal longitude and latitude values , that is , 90< latitude <-90, 180 < longitude < -180."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.436090Z",
     "start_time": "2022-01-26T20:30:29.286395Z"
    }
   },
   "outputs": [],
   "source": [
    "incorrect_coordinates = df_taxi.loc[(df_taxi.latitude_of_pickup > 90) |(df_taxi.latitude_of_pickup < -90) |\n",
    "                                   (df_taxi.latitude_of_dropoff > 90) |(df_taxi.latitude_of_dropoff < -90) |\n",
    "                                   (df_taxi.longitude_of_pickup > 180) |(df_taxi.longitude_of_pickup < -180) |\n",
    "                                   (df_taxi.longitude_of_dropoff > 90) |(df_taxi.longitude_of_dropoff < -90)\n",
    "                                    ].index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.679373Z",
     "start_time": "2022-01-26T20:30:29.436090Z"
    }
   },
   "outputs": [],
   "source": [
    "df_taxi.drop(incorrect_coordinates, inplace = True, errors = 'ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.804152Z",
     "start_time": "2022-01-26T20:30:29.679373Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Remaining observastions in the dataset: (49989, 12)\n"
     ]
    }
   ],
   "source": [
    "print(\"Remaining observastions in the dataset:\", df_taxi.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> The number of observations is reduced to 48455 from 50000 which suggests that we have removed the observations with extreme or immpractical values.\n",
    "                    </b>   \n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "BudwXJ6Kebou"
   },
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"alsoreadicon.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>I love to know more:  </b><a href=\"https://bit.ly/33bgNpq\">How to use statistics to identify outliers in data</a>\n",
    "</font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Missing_Values'></a>\n",
    "### 4.1.5 Missing Values\n",
    "\n",
    "If the missing values are not handled properly we may end up drawing an inaccurate inference about the data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>In order to get the count of missing values in each column.<br><br>\n",
    "                        <ol type=\"1\"><li>Check the missing values</li>\n",
    "                            <li>Visualize missing values using heatmap</li>\n",
    "                            <li>Handle missing values\n",
    "                            <ul type=\"i\">\n",
    "                                <li>For numeric variables</li>\n",
    "                                <li> For categoric variables</li>\n",
    "                            </ul>\n",
    "                        </ol>  </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Check the missing values**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:29.943660Z",
     "start_time": "2022-01-26T20:30:29.816119Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Total</th>\n",
       "      <th>Percentage of Missing Values</th>\n",
       "      <th>Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>amount</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>float64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>float64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>float64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>float64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>float64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no_of_passenger</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>int64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hour</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>int64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>day</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>int64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>month</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>int64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>int64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dayofweek</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>int64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>travel_dist_km</th>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>float64</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      Total  Percentage of Missing Values     Type\n",
       "amount                    0                      0.000000  float64\n",
       "longitude_of_pickup       0                      0.000000  float64\n",
       "latitude_of_pickup        0                      0.000000  float64\n",
       "longitude_of_dropoff      0                      0.000000  float64\n",
       "latitude_of_dropoff       0                      0.000000  float64\n",
       "no_of_passenger           0                      0.000000    int64\n",
       "hour                      0                      0.000000    int64\n",
       "day                       0                      0.000000    int64\n",
       "month                     0                      0.000000    int64\n",
       "year                      0                      0.000000    int64\n",
       "dayofweek                 0                      0.000000    int64\n",
       "travel_dist_km            0                      0.000000  float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# sort the variables on the basis of total null values in the variable\n",
    "# 'isnull().sum()' returns the number of missing values in each variable\n",
    "# 'ascending = False' sorts values in the descending order\n",
    "# the variable with highest number of missing values will appear first\n",
    "Total = df_taxi.isnull().sum().sort_values(ascending = False)          \n",
    "\n",
    "# calculate the percentage of missing values\n",
    "# 'ascending = False' sorts values in the descending order\n",
    "# the variable with highest percentage of missing values will appear first\n",
    "Percent = (df_taxi.isnull().sum()*100/df_taxi.isnull().count()).sort_values(ascending = False)   \n",
    "\n",
    "# concat the 'Total' and 'Percent' columns using 'concat' function\n",
    "# 'keys' is the list of column names\n",
    "# 'axis = 1' concats along the columns\n",
    "missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    \n",
    "\n",
    "# add the column containing data type of each variable\n",
    "missing_data['Type'] = df_taxi[missing_data.index].dtypes\n",
    "missing_data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>None of the variables contain missing values.</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Visualize missing values using heatmap**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:33.579149Z",
     "start_time": "2022-01-26T20:30:29.943660Z"
    },
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plot heatmap to visualize the null values in each column\n",
    "# 'cbar = False' does not show the color axis \n",
    "sns.heatmap(df_taxi.isnull(), cbar=False)\n",
    "\n",
    "# display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If there are missing values in a dataset then the horizontal lines in the heatmap correspond to the missing values. Since there are no missing values here there are no horizontal lines corresponding to them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Dogz55FZeboP"
   },
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> The above plot shows that there are no missing values in the data.</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='correlation'></a>\n",
    "### 4.1.6 Study correlation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "K_oo8YEAeboS"
   },
   "source": [
    "Correlation is a statistic that measures the degree to which two variables move with each other. A correlation coefficient near  1  indicates the strong relationship between them; a weak correlation indicates the extent to which one variable increases as the other decreases. Correlation among multiple variables can be represented in the form of a matrix. This allows us to see which variables are correlated."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "sAagGX-keboT"
   },
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> To check the correlation between numerical variables, we perform the following steps:<br><br>\n",
    "                    1. Compute a correlation matrix  <br>\n",
    "                    2. Plot a heatmap for the correlation matrix\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Compute a correlation matrix**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:33.673032Z",
     "start_time": "2022-01-26T20:30:33.579149Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>amount</th>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <th>no_of_passenger</th>\n",
       "      <th>hour</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>dayofweek</th>\n",
       "      <th>travel_dist_km</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>amount</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.005905</td>\n",
       "      <td>-0.006563</td>\n",
       "      <td>0.004452</td>\n",
       "      <td>-0.005600</td>\n",
       "      <td>0.016506</td>\n",
       "      <td>-0.022009</td>\n",
       "      <td>-0.001417</td>\n",
       "      <td>0.026742</td>\n",
       "      <td>0.121081</td>\n",
       "      <td>0.000542</td>\n",
       "      <td>0.016451</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <td>0.005905</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.984132</td>\n",
       "      <td>0.956613</td>\n",
       "      <td>-0.947401</td>\n",
       "      <td>-0.005614</td>\n",
       "      <td>0.004913</td>\n",
       "      <td>0.006008</td>\n",
       "      <td>0.000402</td>\n",
       "      <td>-0.001264</td>\n",
       "      <td>-0.003224</td>\n",
       "      <td>0.143712</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <td>-0.006563</td>\n",
       "      <td>-0.984132</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.943741</td>\n",
       "      <td>0.961374</td>\n",
       "      <td>0.003982</td>\n",
       "      <td>-0.004313</td>\n",
       "      <td>-0.008884</td>\n",
       "      <td>0.000498</td>\n",
       "      <td>-0.000925</td>\n",
       "      <td>0.001911</td>\n",
       "      <td>-0.130943</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <td>0.004452</td>\n",
       "      <td>0.956613</td>\n",
       "      <td>-0.943741</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.982102</td>\n",
       "      <td>-0.004874</td>\n",
       "      <td>0.005506</td>\n",
       "      <td>0.005221</td>\n",
       "      <td>0.001322</td>\n",
       "      <td>-0.000327</td>\n",
       "      <td>-0.002441</td>\n",
       "      <td>0.143172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <td>-0.005600</td>\n",
       "      <td>-0.947401</td>\n",
       "      <td>0.961374</td>\n",
       "      <td>-0.982102</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.002898</td>\n",
       "      <td>-0.004530</td>\n",
       "      <td>-0.008012</td>\n",
       "      <td>-0.000341</td>\n",
       "      <td>-0.001817</td>\n",
       "      <td>0.001626</td>\n",
       "      <td>-0.124844</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no_of_passenger</th>\n",
       "      <td>0.016506</td>\n",
       "      <td>-0.005614</td>\n",
       "      <td>0.003982</td>\n",
       "      <td>-0.004874</td>\n",
       "      <td>0.002898</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011400</td>\n",
       "      <td>0.006787</td>\n",
       "      <td>0.009099</td>\n",
       "      <td>0.006385</td>\n",
       "      <td>0.038581</td>\n",
       "      <td>-0.005371</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hour</th>\n",
       "      <td>-0.022009</td>\n",
       "      <td>0.004913</td>\n",
       "      <td>-0.004313</td>\n",
       "      <td>0.005506</td>\n",
       "      <td>-0.004530</td>\n",
       "      <td>0.011400</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.008192</td>\n",
       "      <td>-0.001916</td>\n",
       "      <td>0.004167</td>\n",
       "      <td>-0.091267</td>\n",
       "      <td>0.000644</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>day</th>\n",
       "      <td>-0.001417</td>\n",
       "      <td>0.006008</td>\n",
       "      <td>-0.008884</td>\n",
       "      <td>0.005221</td>\n",
       "      <td>-0.008012</td>\n",
       "      <td>0.006787</td>\n",
       "      <td>-0.008192</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.017266</td>\n",
       "      <td>-0.011155</td>\n",
       "      <td>0.008422</td>\n",
       "      <td>0.010610</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>month</th>\n",
       "      <td>0.026742</td>\n",
       "      <td>0.000402</td>\n",
       "      <td>0.000498</td>\n",
       "      <td>0.001322</td>\n",
       "      <td>-0.000341</td>\n",
       "      <td>0.009099</td>\n",
       "      <td>-0.001916</td>\n",
       "      <td>-0.017266</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.115726</td>\n",
       "      <td>-0.010004</td>\n",
       "      <td>-0.009217</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <td>0.121081</td>\n",
       "      <td>-0.001264</td>\n",
       "      <td>-0.000925</td>\n",
       "      <td>-0.000327</td>\n",
       "      <td>-0.001817</td>\n",
       "      <td>0.006385</td>\n",
       "      <td>0.004167</td>\n",
       "      <td>-0.011155</td>\n",
       "      <td>-0.115726</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.006808</td>\n",
       "      <td>0.022136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dayofweek</th>\n",
       "      <td>0.000542</td>\n",
       "      <td>-0.003224</td>\n",
       "      <td>0.001911</td>\n",
       "      <td>-0.002441</td>\n",
       "      <td>0.001626</td>\n",
       "      <td>0.038581</td>\n",
       "      <td>-0.091267</td>\n",
       "      <td>0.008422</td>\n",
       "      <td>-0.010004</td>\n",
       "      <td>0.006808</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.000518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>travel_dist_km</th>\n",
       "      <td>0.016451</td>\n",
       "      <td>0.143712</td>\n",
       "      <td>-0.130943</td>\n",
       "      <td>0.143172</td>\n",
       "      <td>-0.124844</td>\n",
       "      <td>-0.005371</td>\n",
       "      <td>0.000644</td>\n",
       "      <td>0.010610</td>\n",
       "      <td>-0.009217</td>\n",
       "      <td>0.022136</td>\n",
       "      <td>-0.000518</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        amount  longitude_of_pickup  latitude_of_pickup  \\\n",
       "amount                1.000000             0.005905           -0.006563   \n",
       "longitude_of_pickup   0.005905             1.000000           -0.984132   \n",
       "latitude_of_pickup   -0.006563            -0.984132            1.000000   \n",
       "longitude_of_dropoff  0.004452             0.956613           -0.943741   \n",
       "latitude_of_dropoff  -0.005600            -0.947401            0.961374   \n",
       "no_of_passenger       0.016506            -0.005614            0.003982   \n",
       "hour                 -0.022009             0.004913           -0.004313   \n",
       "day                  -0.001417             0.006008           -0.008884   \n",
       "month                 0.026742             0.000402            0.000498   \n",
       "year                  0.121081            -0.001264           -0.000925   \n",
       "dayofweek             0.000542            -0.003224            0.001911   \n",
       "travel_dist_km        0.016451             0.143712           -0.130943   \n",
       "\n",
       "                      longitude_of_dropoff  latitude_of_dropoff  \\\n",
       "amount                            0.004452            -0.005600   \n",
       "longitude_of_pickup               0.956613            -0.947401   \n",
       "latitude_of_pickup               -0.943741             0.961374   \n",
       "longitude_of_dropoff              1.000000            -0.982102   \n",
       "latitude_of_dropoff              -0.982102             1.000000   \n",
       "no_of_passenger                  -0.004874             0.002898   \n",
       "hour                              0.005506            -0.004530   \n",
       "day                               0.005221            -0.008012   \n",
       "month                             0.001322            -0.000341   \n",
       "year                             -0.000327            -0.001817   \n",
       "dayofweek                        -0.002441             0.001626   \n",
       "travel_dist_km                    0.143172            -0.124844   \n",
       "\n",
       "                      no_of_passenger      hour       day     month      year  \\\n",
       "amount                       0.016506 -0.022009 -0.001417  0.026742  0.121081   \n",
       "longitude_of_pickup         -0.005614  0.004913  0.006008  0.000402 -0.001264   \n",
       "latitude_of_pickup           0.003982 -0.004313 -0.008884  0.000498 -0.000925   \n",
       "longitude_of_dropoff        -0.004874  0.005506  0.005221  0.001322 -0.000327   \n",
       "latitude_of_dropoff          0.002898 -0.004530 -0.008012 -0.000341 -0.001817   \n",
       "no_of_passenger              1.000000  0.011400  0.006787  0.009099  0.006385   \n",
       "hour                         0.011400  1.000000 -0.008192 -0.001916  0.004167   \n",
       "day                          0.006787 -0.008192  1.000000 -0.017266 -0.011155   \n",
       "month                        0.009099 -0.001916 -0.017266  1.000000 -0.115726   \n",
       "year                         0.006385  0.004167 -0.011155 -0.115726  1.000000   \n",
       "dayofweek                    0.038581 -0.091267  0.008422 -0.010004  0.006808   \n",
       "travel_dist_km              -0.005371  0.000644  0.010610 -0.009217  0.022136   \n",
       "\n",
       "                      dayofweek  travel_dist_km  \n",
       "amount                 0.000542        0.016451  \n",
       "longitude_of_pickup   -0.003224        0.143712  \n",
       "latitude_of_pickup     0.001911       -0.130943  \n",
       "longitude_of_dropoff  -0.002441        0.143172  \n",
       "latitude_of_dropoff    0.001626       -0.124844  \n",
       "no_of_passenger        0.038581       -0.005371  \n",
       "hour                  -0.091267        0.000644  \n",
       "day                    0.008422        0.010610  \n",
       "month                 -0.010004       -0.009217  \n",
       "year                   0.006808        0.022136  \n",
       "dayofweek              1.000000       -0.000518  \n",
       "travel_dist_km        -0.000518        1.000000  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# use the corr() function to generate the correlation matrix of the numeric variables\n",
    "corr = df_taxi.corr()\n",
    "\n",
    "# print the correlation matrix\n",
    "corr"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Plot the heatmap for the diagonal correlation matrix**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A correlation matrix is a symmetric matrix. Plot only the upper triangular entries using a heatmap."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:35.649061Z",
     "start_time": "2022-01-26T20:30:33.675027Z"
    },
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 2880x1440 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# set the plot size\n",
    "# pass the required height and width to the parameter, 'figsize'  \n",
    "plt.figure(figsize = (40,20))\n",
    "\n",
    "# use 'mask' to plot a upper triangular correlation matrix \n",
    "# 'tril_indices_from' returns the indices for the lower-triangle of matrix\n",
    "# 'k = -1' consider the diagonal of the matrix\n",
    "mask = np.zeros_like(corr)\n",
    "mask[np.tril_indices_from(mask, k = -1)] = True\n",
    "\n",
    "# plot the heat map\n",
    "# corr: give the correlation matrix\n",
    "# cmap: color code used for plotting\n",
    "# vmax: gives a maximum range of values for the chart\n",
    "# vmin: gives a minimum range of values for the chart\n",
    "# annot: prints the correlation values in the chart\n",
    "# annot_kws: sets the font size of the annotation\n",
    "# mask: mask the upper traingular matrix values\n",
    "sns.heatmap(corr, cmap = 'RdYlGn', vmax = 1.0, vmin = -1.0, annot = True, annot_kws = {\"size\": 20}, mask = mask)\n",
    "\n",
    "# set the size of x and y axes labels\n",
    "# set text size using 'fontsize'\n",
    "plt.xticks(fontsize = 12)\n",
    "plt.yticks(fontsize = 15)\n",
    "\n",
    "# display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>The diagonal entries are all '1' which represents the correlation of the variable with itself. The dark green squares represent the variables with strong positive correlation. The dark red squares represent the variables with strong negative correlation. \n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As the above correlation map is difficult to study. Create a heatmap that consider the variables with strong correlation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:36.540610Z",
     "start_time": "2022-01-26T20:30:35.652054Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 3600x1440 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# set figure size\n",
    "plt.figure(figsize=(50, 20))\n",
    "\n",
    "# plot the heat map\n",
    "# corr: give the correlation matrix\n",
    "# pass the condition to get the strong correlation between the variables\n",
    "# cmap: color code used for plotting\n",
    "# vmax: gives a maximum range of values for the chart\n",
    "# vmin: gives a minimum range of values for the chart\n",
    "# annot: prints the correlation values in the chart\n",
    "# annot_kws: sets the font size of the annotation\n",
    "#sns.set(font_scale=2)\n",
    "sns.heatmap(corr[(corr >= 0.7) | (corr <= -0.7)], cmap = 'RdYlGn', vmax = 1.0, vmin = -1.0, annot = True, \n",
    "            annot_kws={\"size\": 20})\n",
    "\n",
    "# set the size of x and y axes labels\n",
    "# set text size using 'fontsize'\n",
    "plt.xticks(fontsize = 15)\n",
    "plt.yticks(fontsize = 15)\n",
    "\n",
    "# display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>The above plot shows that there is highest positive correlation (= 0.96) between the variables 'longitude_of_pickup' and 'longitude_of_dropoff'. Also there is strong positive correlation between the pair latitude_of_pickup and latitude_of_dropoff. These variables may be involved in multicollinearity.<br>\n",
    "                        Following variable pairs have strong negative correlation in the dataset(longitude_of_pickup,latitude_of_pickup), (latitude_of_dropoff,longitude_of_pickup),(longitude_of_dropoff,latitude_of_pickup) and (longitude_of_dropoff, latitude_of_dropoff).\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "pPwoQF_Hebod"
   },
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"quicktip.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Correlation does not imply causation. In other words, if two variables are correlated, it does not mean that one variable caused the other.</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "OET43huSeboe"
   },
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"alsoreadicon.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>I love to know more:</b> <br><br>\n",
    "                    <a href=\"https://bit.ly/2PBvA8T\">Why correlation does not imply causation </a>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='EDA'></a>\n",
    "## 4.2 Exploratory Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Peak'></a>\n",
    "### 4.2.1 Peak hours"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will check for the business during the weekdays and weekends."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> We will check the peak hours during the following: <br><br>\n",
    "                        1. Weekdays <br>\n",
    "                        2. Weekends <br>\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Plot a countplot to check the peak hours during weekdays**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To plot a countplot, we use the `countplot()` from the seaborn library."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:37.099415Z",
     "start_time": "2022-01-26T20:30:36.540610Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Taxi trips count during week days'}, xlabel='hour', ylabel='count'>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set the figure size, grid type and color palette along with appropraite titel for the plot\n",
    "plt.figure(figsize=(20,5))\n",
    "plt.title('Taxi trips count during week days')\n",
    "sns.set_style(\"white\")\n",
    "#plot the countplot for weekdays\n",
    "sns.countplot(x='hour', data=df_taxi.loc[(df_taxi.dayofweek >= 0) & (df_taxi.dayofweek <=4)], palette='Set2')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that during the weekdays the count of trips start to peak from 8 am and is highest at 9am. In the evening the peak is at 6pm and 7pm."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Plot a countplot to check the peak hours during weekends**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:37.626404Z",
     "start_time": "2022-01-26T20:30:37.099415Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Taxi trips count during week ends'}, xlabel='hour', ylabel='count'>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABI8AAAFJCAYAAAASfA0MAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAA0n0lEQVR4nO3de1xUdeL/8fdcGDQumlvuVopBSqVFaiYV3svQVvOSIgyLkXaRrlBr4AWwvLfGZu2a2qPLL6jI1LTtZkUmeYlcKk2LLcmszMy8JIOGXM7vj77NinB0RMcD7uv518yZM2feZxznzLz5fM7YDMMwBAAAAAAAANTDbnUAAAAAAAAANF6URwAAAAAAADBFeQQAAAAAAABTlEcAAAAAAAAwRXkEAAAAAAAAU5RHAAAAAAAAMEV5BADA/6hp06ZpyJAhGjJkiC655BLFxsZ6r//666/Hta1JkyZp7dq1dZa///77mjt3br33KSgo0LRp0xqU3SpH25/D7dmzRxdeeOFxb3/u3LlatmxZA5KdOkVFRRo0aNApeayHHnpIjz/++Cl5LAAAYM5pdQAAAGCNyZMney/369dPc+bM0aWXXtqgbU2fPr3e5Z999pl++eWXem+75pprdM011zTo8axytP05Ge69916/bRsAAKChKI8AAEAtBw4c0JQpU7Rt2zbt27dPQUFBmjNnjs4991zdeOONcrvdSkxM1Msvv6znnntOixYt0m233abExEQNGDDAu50NGzYoPz9f1dXVCgkJUbt27bR48WIdPHhQwcHBGjZsmFasWKEFCxYoKSlJHTt2VHFxsfbu3ashQ4bonnvuUVVVlaZOnaqPP/5YAQEBatOmjWbOnKmgoKBamXft2qXs7Gx9/fXXstvtio+P1+jRo/Xjjz9qypQp2r59uwzD0NChQ3XLLbfo+++/1+DBg/XJJ59IUq3rS5cu1TvvvCO73a5t27apWbNmmj17tjweT639SUtLq5Xh7bff1t///nc1b95cl1xyiXf50qVLvft55PWMjAzt27dP3333nfr06aPdu3erQ4cOGjt2rC699FLddtttWrNmjX766Sfdcsstcrvdqq6u1sMPP6z33ntPISEhioqKUmlpqXJzc72PWV1drZiYGL300ktq166dFixYoPz8fK1cuVKSlJycrJtvvlldu3bV9OnT9eWXX6qyslJXXXWVHnjgATmdTpWWlmr69Onat2+fqqurlZSUpBEjRtTa53//+9/661//qpycHHXt2rXWbTt37tRDDz2kHTt2qLKyUn/+8581btw4ff/990pOTlbv3r21YcMG7d+/X+PHj1f//v3l8Xg0adIklZSUqHXr1nI4HLr88sslSS+88ILy8/MVEBCgwMBAPfTQQ2rfvn2DXuMAAOD4UB4BAIBaCgsLFRoaqpdeekmSlJWVpeeff16ZmZnKycnR6NGj1aZNGz366KPKzc1V8+bN693OZZddpvj4eO3du1dpaWlaunSptmzZovfee0/BwcFaunRprfW3bt2qF198UQcPHlRcXJwuvfRShYSE6KOPPtIbb7whm82mv/3tb/rPf/5Tp6h48MEHdf7552vevHkqKytTQkKCevfurUmTJumaa67RzTffrLKyMiUmJuqcc87RZZdddtTnYP369Xrttdf0pz/9SVOnTtXChQs1e/bsWvtzuJ9//lkTJ05Ufn6+2rdv7y2KfPHrr7/q9ddflyRlZGR4lx86dEhnnnmm8vPztWnTJiUkJOjGG2/UK6+8os2bN+u1116TzWZTSkpKnW06HA717dtXH3zwgdq1a6cPPvhAlZWV2rp1q8466yyVlJToqquuUnZ2tjp16qRZs2apurpaGRkZeuaZZ3TzzTfrnnvu0cMPP6xOnTqprKxMo0aNqlXWfPjhh8rMzNT8+fN10UUX1ckwfvx4JScnq1+/fqqoqNCtt96qsLAwRUVF6bvvvlOPHj2UmZmpFStWaMaMGerfv78ee+wxNWvWTG+99Zb27t2rYcOG6fLLL1d1dbVmzJih9957T61bt9ayZctUXFxMeQQAwClCeQQAAGoZMGCA2rZtq9zcXG3btk0fffSRunTpIkm68MILddddd+n222/XrFmzFBERcVzbvvDCCxUcHFzvbaNGjVJAQIACAgI0YMAArV69Wvfee68cDodGjhypHj16KDY2VlFRUXXuu3btWo0fP16SFBISotdee00HDhzQxx9/rKefftq7fPjw4SosLDxmedSpUyf96U9/kiR17NhR77zzzlHXLy4uVmRkpLfMGDVqlHJyco7+ZPyf30fW1Of3aX2dOnXSoUOHdODAAa1atUpDhgxRYGCg97EOH3X0u/79+ys/P19Dhw7Vrl27NGjQIK1du1YtWrRQz5495XK59P777+uzzz7T4sWLJcl7rqtvvvlG3377rSZOnOjd3q+//qrPP/9cF1xwgX788UeNGzdOCQkJ9RZHBw4c0Pr16/XLL794zxF14MABlZSUKCoqSgEBAerdu7ek357fffv2SZLWrVuniRMnymazqVWrVurfv7+k38qwAQMGKD4+Xn369FGPHj289wcAAP5HeQQAAGp54YUXtGjRIiUmJmrw4MFq2bKlvv/+e+/tX331lc466yxt2LBBQ4cOPa5tn3HGGaa3OZ3//VhiGIbsdrtCQ0O1fPlyffzxx/rwww+VmpqqsWPHKjExsc59bTab9/p3332nli1byjCMWuvV1NSoqqpKNput1m2VlZW11mvWrJn38pHrmjl8ncP35ViPdbTn5PeC6Pd9Mwyj1rYlyW6v//dPYmJiNHnyZK1atUrR0dG6+uqr9eKLL6p58+a6/vrrJf32fMydO1cXXHCBJGn//v2y2Wz64YcfFBISouXLl3u39/PPPyskJESffvqpHA6HFi5cqDvuuEMDBgyoU8bV1NTIMAzl5+d7R6bt2bNHgYGB2rt3rwICAry5D/93+30ff+dwOLyX58yZoy+//FJr167VwoULtXz5cp9OXg4AAE4cv7YGAABqWb16tYYNG6aRI0cqPDxc7733nqqrqyX9dl6foqIivfrqq1qzZo3efffdo27L4XCoqqrKp8d99dVXVVNTo19++UVvvvmm+vXrp5UrVyo5OVldunTR3XffraFDh2rTpk117nvVVVdpyZIlkqSysjLddNNN2rZtmy677DI9//zz3uXLli3T1VdfrdDQUFVWVmrLli2S5J02dixm+3PFFVdoy5YtKikpkaRaU/JatWqlr776ShUVFaqsrNSKFSt8eiwzvXv31quvvqpDhw6pqqpKr7zySr3rBQYG6oorrtA//vEPxcTEqHv37vr000/173//Wz179pQk9ejRQ88++6wMw9ChQ4eUkpKivLw8hYeHq1mzZt7yaMeOHRo0aJD3uT/77LPVtWtXpaen64EHHtDBgwdrPXZwcLA6d+6sZ555RtJvpVRCQoIKCgqOum89e/bU4sWLva+D39ffs2ePevfurZYtWyo5OVmpqan67LPPGv4kAgCA40J5BAAAahkzZoxeeuklDR48WImJierUqZO+/fZb7dixQ9nZ2Xr44YfVqlUrzZo1S5mZmfrxxx9Nt3XllVdq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\n",
      "text/plain": [
       "<Figure size 1440x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set the figure size, grid type and color palette along with appropraite titel for the plot\n",
    "plt.figure(figsize=(20,5))\n",
    "plt.title('Taxi trips count during week ends')\n",
    "sns.set_style(\"white\")\n",
    "#plot the countplot for weekends\n",
    "sns.countplot(x='hour', data=df_taxi.loc[(df_taxi.dayofweek >= 5) & (df_taxi.dayofweek <=6)], palette='Set2')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that during the weekends the count of trips is high after 12 midnight to 3am to 4am. This pattern is different from the weekdays. In the evening the demand is almost evenly high after 6pm till late night except."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>From the above plot, we can notice that the pattern for demand of taxi is different for weekdays and weekends.</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Mean_Fare'></a>\n",
    "### 4.2.2 Mean fare for each hour during weekdays and weekends"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will check the mean fares for each hour during the weekdays and weekends."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> We will do the following: <br><br>\n",
    "                        1. Compute the mean hourly fare for weekdays and weekends <br>\n",
    "                        2. Plot the bar graph for the same <br>\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Compute the hourly mean fare for weekdays and weekends**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:37.734505Z",
     "start_time": "2022-01-26T20:30:37.628335Z"
    }
   },
   "outputs": [],
   "source": [
    "# Set the days in the dataset as week days and week ends\n",
    "week_days = df_taxi.loc[(df_taxi.dayofweek >= 0) & (df_taxi.dayofweek <= 4)]\n",
    "week_ends = df_taxi.loc[(df_taxi.dayofweek >= 5) & (df_taxi.dayofweek <= 6)]\n",
    "# compute the mean fare amount over the week day and week end.\n",
    "# use groupby('hour') to get the mean fare for each hour\n",
    "week_days_fare = week_days.groupby(['hour']).amount.mean().to_frame().reset_index()\n",
    "week_ends_fare = week_ends.groupby(['hour']).amount.mean().to_frame().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:37.827708Z",
     "start_time": "2022-01-26T20:30:37.734505Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>hour</th>\n",
       "      <th>amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>12.079275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>12.522360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>10.929956</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>11.837477</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>14.961357</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>15.502702</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6</td>\n",
       "      <td>11.438986</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7</td>\n",
       "      <td>10.863713</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8</td>\n",
       "      <td>10.468992</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>9</td>\n",
       "      <td>10.699696</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>10</td>\n",
       "      <td>11.200024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>11</td>\n",
       "      <td>11.305669</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>12</td>\n",
       "      <td>11.481385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>13</td>\n",
       "      <td>11.705997</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>14</td>\n",
       "      <td>12.222706</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>15</td>\n",
       "      <td>12.059795</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>16</td>\n",
       "      <td>12.525304</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>17</td>\n",
       "      <td>11.426644</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>18</td>\n",
       "      <td>11.014698</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>19</td>\n",
       "      <td>10.755850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>20</td>\n",
       "      <td>10.786913</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>21</td>\n",
       "      <td>11.293807</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>22</td>\n",
       "      <td>11.061567</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>23</td>\n",
       "      <td>11.311165</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    hour    amount\n",
       "0      0 12.079275\n",
       "1      1 12.522360\n",
       "2      2 10.929956\n",
       "3      3 11.837477\n",
       "4      4 14.961357\n",
       "5      5 15.502702\n",
       "6      6 11.438986\n",
       "7      7 10.863713\n",
       "8      8 10.468992\n",
       "9      9 10.699696\n",
       "10    10 11.200024\n",
       "11    11 11.305669\n",
       "12    12 11.481385\n",
       "13    13 11.705997\n",
       "14    14 12.222706\n",
       "15    15 12.059795\n",
       "16    16 12.525304\n",
       "17    17 11.426644\n",
       "18    18 11.014698\n",
       "19    19 10.755850\n",
       "20    20 10.786913\n",
       "21    21 11.293807\n",
       "22    22 11.061567\n",
       "23    23 11.311165"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "week_days_fare"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Plot the mean fare**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:38.459105Z",
     "start_time": "2022-01-26T20:30:37.829670Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABIkAAAJZCAYAAAAtXGVNAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABFhklEQVR4nO3deZid48E/8O9kEyQaSVESNNFaWkWlpEhCUCSVIIIII2n0h6BaW7OIrST2lKb1Wl6qDaWxtKit9lgj9i2W2IMGCZWEbDPP7w+XeUUymYjMORP5fK5rritne+7veXJmnjnfuZ/7VBRFUQQAAACA5VqjcgcAAAAAoPyURAAAAAAoiQAAAABQEgEAAAAQJREAAAAAURIBAAAAECURAN8QkydPzgYbbJD9999/gduGDBmSDTbYINOmTav3HEOGDEmXLl2y2267zfc1ZcqUehvzxRdfzAYbbJCLLrqo3sZYmIEDBy50n44fPz6bbLLJAvvgyiuv/FrjbbDBBunZs+cC2508efISbW/IkCG55JJL6rzfddddl4MPPniB6ysrK3Prrbcu0dhfx0033ZTdd999vuv22WefdOnSJUVR1Fz3//7f/8vf/va3JRpj/Pjx2XXXXeu836233prKysolGmNxvPXWW9l4440X+v3Ts2fP3H777Yu1nQMPPDB/+ctfai6/9tpr2WCDDTJq1Kia66ZOnZqNN94406dPX6Ksi/t6WhL1vZ8B4HNNyh0AAJaWFVZYIa+99lrefvvttG3bNknyySef5PHHHy9pjgEDBuTAAw8s2Xh/+9vf0rNnz1xxxRUZOHBgmjQpzeH9gQceqPW2ddZZJ9dff/1SH/Mvf/lLWrduvdS3uyzZZpttMnjw4Hz00Udp1apVpk2blvfeey9t2rTJM888k0022STz5s3LY489lpNOOqnccb+WtddeO1tvvXWuu+66DBo0qOb6J554ItOnT8/222+/WNvp2rVrxo8fn/79+ydJ7r777nTr1i133nlnjjrqqCTJww8/nM033zwtW7Zc+k8EAJYRZhIB8I3RuHHjdO/ePTfeeGPNdf/+97+zww47zHe/u+66K3vttVd233339O3bN0888USS5IMPPsihhx6affbZJ9tvv30qKyszderUJMn222+f0aNHp1+/funWrVvOPffcr5zvtddeyy9+8Yvsvffe6datWwYNGpTZs2cnSTbeeOP8+te/zs4775xnnnkmr7zySgYOHJjevXtnt912yzXXXLPQbc6YMSM33nhjBg0alJYtW+a2226ruW306NE59thjc8ABB6R79+455phjcvXVV2e//fbLtttum3/9619Jkrlz5+aUU05Jjx490rNnzxx33HGZMWPGIp/30KFDkyT9+/fPu++++5X2w9///vfsuuuu6dWrVwYOHJjXXnstyWczMQ455JD8/Oc/z1lnnfWVtlldXZ1TTz01e+21V3r06JHu3bvnscceS5LMnDkzQ4cOzc4775wePXpk1KhRNTNunnjiifTt2zc77rhjBg0alE8++eQrjfu5Rx99NHvvvXd69uyZ3r17Z9y4cUkWnIX0xctL+nxbtWqVjTfeOI8++miS5J577knnzp2z3Xbb5a677kqSPPXUU2nbtm3atm2b6dOnZ8iQIendu3d69uyZkSNHZt68eUmyWK+zRx99NNttt11N2Xreeedlxx13TJ8+feabyVPb6/uGG25I3759a+73zjvvpHPnzpkzZ07+8Ic/1OyzAw88MO+9994C4++333657rrr5pslNXbs2PTt2zeNGzfOo48+mj59+qR3797p3bv3fN8Dn+vatWseffTRVFdXJ/msJDrooIMyc+bMvPnmm0mShx56KNttt12S5PHHH0+/fv2yxx57ZM8998zdd99ds62rr746vXv3zu67754BAwbklVdeWWC8kSNHpn///pk5c2bmzJmTkSNHZo899kivXr0yZMiQOr+/FrWfF+f5AsASKwDgG+Ctt94qNttss+KZZ54pdtlll5rr+/fvX7z44ovF+uuvX0ydOrV47bXXil133bWYNm1aURRF8dJLLxXbbLNNMXPmzOKyyy4rLrzwwqIoiqK6urr45S9/WVxyySVFURRFt27ditNPP70oiqL4z3/+U/zoRz8q3nzzzQVyDB48uOjcuXPRq1evmq+xY8cWRVEUp59+evHPf/6zKIqimDNnTrHrrrsWt956a1EURbH++usX//jHP4qiKIq5c+cWPXr0KJ599tmiKIri448/Lrp371488cQTC4x3+eWXF3vssUdRFEVx8cUXF3369Km57Q9/+EPRrVu34uOPPy4+/fTTYosttihOO+20oiiK4vbbby922mmnoiiK4rzzzisOP/zwYs6cOUVVVVUxZMiQ4vjjj6/zeX++T7/s4YcfLn70ox/Ntw8OPvjgoiiK4sEHHyx23HHHmsdde+21Rffu3Yvq6upi8ODBRf/+/RfY3ufWX3/9Ytddd51vu4ceemhRFEXx+OOPF7/61a+KqqqqoiiK4sILL6wZc+TIkcWRRx5ZzJs3r5g9e3ax3377FQ8//HAxePDgok+fPsUnn3xSzJs3r9hjjz1q/g++6Nprry0233zz+cbt1atXsdlmmxW33HJLMW3atGKrrbYqnnzyyaIoPntNbbnllsWbb75ZXHvttcVBBx0037Y+v1zX812UP/7xj8Wpp55aFEVRHH744cUdd9xRPPHEE0XPnj2LoiiK0aNHF2eddVZRFEUxZMiQ4q9//WtRFEUxb9684phjjikuuuiiRb7OHn744eLnP/958dBDDxU77rhjMXHixKIoPnvd9OjRo5g+fXoxd+7c4qCDDir233//oihqf33Pnj272GqrrYqXXnqpKIqiOPfcc4uzzz67eOedd4rNN9+8mD17dlEURXHJJZcUt99++wLPtaqqqthhhx2Khx9+uCbnFltsUXzwwQdFURTFAQccUPzrX/8qiqIoJk6cWJx00kkL3Wc77LBD8fzzzxcfffRRsc022xRVVVXF8ccfX/z5z38uiqIott9++2LSpEnFRx99VOy0007FW2+9VRTFZ6/7rl27Fm+//XYxfvz4ol+/fsUnn3xSFEVR3HfffTU/bwYPHlxcfPHFxcknn1wcdthhNc9r9OjRxemnn15UV1cXRVEU55xzTnHiiScWRVH799ei9vPiPl8AWBJONwPgG2XjjTdO48aN8+yzz6ZNmzaZOXNm1l9//ZrbH3jggbz33nsZMGBAzXUVFRV58803079//zz66KP585//nNdffz0vv/xyNt1005r7fT4jaY011kibNm3y3//+N2uvvfYCGWo73ezYY4/NAw88kIsvvjivv/563nvvvflmrvzkJz9Jkrz++ut58803M2zYsJrbZs2aleeffz6bbbbZfNu86qqrsvfeeydJevXqlVGjRuWJJ57Ij3/84yTJ1ltvXXP6zOqrr54uXbok+ex0sI8++ihJMm7cuBx55JFp2rRpks/W2jnssMO+8vP+otpON7vvvvvSo0ePmlPGevfunREjRtSsK9SxY8dFbre2081+/OMf51vf+lauuuqqvPXWWxk/fnxWXnnlJMmDDz6YoUOHpnHjxmncuHEuv/zyJMk//vGP7LjjjllxxRWTJN///vdrXbfqJz/5SS688ML5rvt8jZinn34666yzTs1r5fvf/34233zzPPLII6moqFjk86nr+dama9euGT58eObMmZNHH300Z555ZlZYYYV88MEH+eCDDzJ+/Pj8+te/TvLZTKNnnnmmZpbQrFmzkiz6dbbeeuvlP//5Tw455JDsu+++2XDDDZN8NtvmZz/7WVq0aJEk2XPPPTNmzJgktb++mzVrlr322itXX311Bg8enH/84x8ZM2ZM1lhjjWy44YbZY4890rVr13Tt2jVbbbXVAs+1UaNG6du3b6699tp06tQpN9xwQ7bddtu0adMmSdK9e/f87ne/y1133ZWtt9665vSxhe2z8ePHp02bNtl6663TqFGjdOvWLVdccUV23HHHVFRUZL311su9996b999/f77vgYqKirz44ouZMGFC3njjjflmRn388cc130uXXXZZpk6dmn/+859p1qxZzf6fPn16HnzwwSSfzdz7PHuy8O+vRe3nxX2+ALAklEQAfOP06tUrN9xwQ1q3bp3ddtttvtuqq6uz1VZbzXdax7vvvpvVV189Z511Vp5++unsueee6dSpU+bNmzffKS4rrLBCzb8rKirmu21xHHXUUamqqkr37t2z3Xbb5d13351vGyuttFKSpKqqKi1btpyvZPnggw8WWCvl0Ucfzcsvv5z//d//zZ///OckSdOmTXPZZZfVlESfv1H93MLWK6qurp6vzKiurs7cuXOX2vP+8lhfVhRFzelPn++Dr+qee+7JiBEj8otf/CI77LBDOnTokBtuuCHJZ8/5i8/v3XffTfPmzWtu+9ySPreqqqoFyqDPn1OzZs3m2+YX92tS+/M977zzak4d23777WsKn89tvPHGmTp1au64445svPHGNUVXly5d8sADD+S1116rKRSrq6tz3nnnZb311kvyWalRUVGRd955p9bX2ZNPPpnGjRvnoosuyqGHHppddtmlpgT74vNp3Lhxzb8X9fru27dv+vTpky233DLf//73a0rGyy+/PM8880weeuihjBw5Ml26dMlvf/vbBfbHnnvumV122SUzZszI2LFjc/LJJ9fc1rdv33Tr1i0PPPBA7rvvvvzxj3/MrbfeOt/rNvmsJLrmmmuywgor1BQzW221VYYPHz7fqWZVVVVZb731cvXVV9c8dsqUKWndunXGjx+f3XbbLccee2zNvn3vvffyrW99K0myxRZbZPPNN8/QoUPz97//PU2bNk11dXWGDRuWbbfdNslnpz9+fpppUvv3V237eXGfLwAsCWsSAfCNs9tuu+XWW2/NzTffvMAnNG211VZ54IEHatYRuffee9OrV6/MmjUr999/f/r375/dd989bdq0yYMPPpiqqqqlluv+++/PYYcdlh49eiT5bN2YhW2/ffv2ad68ec2b93fffTe77rprnn322fnud+WVV2a33XbLvffem7vuuit33XVXLrjggtx+++155513FjtXly5dcuWVV2bu3Lmprq7OFVdckW222abOxzVu3Lim3PkqY9188801M3auvfbatGrVKuuuu+5X2s6XPfDAA+nWrVv69euXjTfeOHfccUfNvt1qq63yj3/8I9XV1ZkzZ06OOOKITJgw4WuN90WbbbZZXn311Tz99NNJkpdffjkTJkzIlltumdatW+fll1/O7NmzM3fu3MVeP+bXv/51rr/++lx//fULFETJZ2XC1ltvnQsuuKCm3EiS7bbbLpdeemm23HLLmgKsc+fOueyyy1IURebMmZNBgwbl8ssvr/N1ttpqq2XzzTfP4MGD89vf/jaffvppunbtmltvvTUff/xxqqur5yuYFvX6XnPNNbPZZptl5MiR2XfffZMkL7zwQnbdddest956OfjggzNgwIA888wzC90fq666arp165Y//OEPady48Xwz6vr27ZuJEyemd+/eOeWUU/Lxxx/n/fffX2AbnTp1ysSJE/PII4/UzKhr3rx5fvjDH+byyy+vKXE222yzvPHGGzWvkYkTJ2bnnXfOlClT0rlz59x00001ayddeeWVNYthJ5+Vd/vvv39atmyZP/7xjzX7/4orrsicOXNSXV2d448/fr5PVVuYRe3nxX2+ALAkzCQC4BtnjTXWyHrrrZeWLVumVatW8932ve99L7/73e9y1FFHpSiKNGnSJP/zP/+TlVdeOYcddljOPPPMnHfeeWnatGk233zzmkVtl4Yjjzwyhx12WFZaaaW0aNEiW2yxxUK336xZs5x//vkZMWJE/vd//zfz5s3Lr3/96/lOTZo2bVr+/e9/59prr53vsVtttVU222yzjBkzZrFn5QwaNChnnHFGdt9998ybNy+bbLJJjj/++Doft8suu6SysjKjR4+e75S+Rdlmm20yYMCA9O/fP9XV1WndunUuvPDCNGq0eH+36t+//wL3Peqoo9K3b98cffTR6dmzZ+bNm5dtttkm//73v1NdXZ3DDz88I0aMyG677Zaqqqr06NEjO+20U81Mna+rdevWOe+883LKKadk1qxZqaioyGmnnZb27dtn7bXXzhZbbJHu3btntdVWS6dOnfLiiy8ulXG7du2a66+/Pt26dau5rnPnzjn22GPzi1/8oua64447LiNGjEjPnj0zd+7cbL311vnlL3+Zpk2b1vo6Gz9+fM3j99hjj9x22205/fTTc/LJJ+fFF1/MnnvumVVWWSUbbrhhPvzwwyR1v74/LzU+L2M23HDDdO/ePXvuuWdWWmmlNG/ePMOHD6/1+fbr1y977713RowYMd/1xxxzTEaOHJlzzz03FRUVOfzww9OuXbsFHr/iiivmu9/9bubOnTvfrLxtt902Z511Vjp16pTks//PP/zhDznzzDMze/bsFEWRM888M+3atUu7du3y//7f/8vAgQNTUVGRFi1a5I9//ON8M8kqKioycuTI7L777tl2221z6KGH5owzzsgee+yRqqqqbLTRRhkyZMgi/2+33XbbWvfz4j5fAFgSFcXXmTMOAAB1qK6uzu9+97ustdZaOeigg8odBwCohdPNAACoNzNmzEinTp3y7rvv5oADDih3HABgEcwkAgAAAMBMIgAAAACURAAAAABESQQAAABAkiblDlCbTp06pW3btuWOAQAAAPCN8fbbb2f8+PELva3BlkRt27bNddddV+4YAAAAAN8YvXv3rvU2p5sBAAAAoCQCAAAAQEkEAAAAQBrwmkQAAADA8mHu3LmZPHlyZs2aVe4o3xjNmzdPu3bt0rRp08V+jJIIAAAAKKvJkyenZcuW+e53v5uKiopyx1nmFUWRqVOnZvLkyWnfvv1iP87pZgAAAEBZzZo1K23atFEQLSUVFRVp06bNV56ZpSQCAAAAyk5BtHQtyf5UEgEAAAANy9Jem6iO7R1wwAF5+umnkyRz5sxJx44dc8kll9Tcvv/+++eFF174SkNus8029XLf+qQkAgAAABqW5s2Tioql99W8+SKH69y5cx599NEkyWOPPZbOnTvnnnvuSZLMnj077777bjbccMP6ftZlpyQCAAAAlmtbb711TUl07733Zq+99sr06dMzffr0PPHEE9lyyy2TJLfcckv22Wef7Lvvvjn77LOTJNOnT88RRxyRysrKVFZW5sUXX5xv26NGjcrJJ5+coihqrquqqsqwYcOy99575+ijj86cOXOSJC+99FIGDhyYAQMGpHfv3nn88cdz//3354gjjqh5bN++ffPee+9lyJAh6devX/bcc8/cfPPNS2U/+HQzAAAAYLn2gx/8IK+++mqKosiECRNy1FFHZauttsqDDz6YF198MV26dMlHH32U0aNH59prr82KK66YY489Ng888EAefPDB/PSnP02/fv3y+uuvZ+jQobnyyiuTJGeccUYqKipy4oknzjfeuHHjMnv27IwdOzbvvPNObrvttiTJpEmTMnjw4GywwQa58cYbc9111+WUU07Jqaeemv/+9795//33s+qqq2allVbK+PHjc+211yZJHnjggaWyH5REAAAAwHKtUaNG2XDDDTNu3ListtpqadasWbp27Zp77rknL7zwQg444IC8+eabmTZtWg466KAkycyZM/PWW2/lpZdeysMPP5xbbrklSfLxxx8nST744IO8+OKLWWeddRYY7+WXX84mm2ySJFlrrbWy5pprJklWX331nH/++WnevHlmzpyZFi1apKKiIr169cq//vWvTJ48OX369EmLFi1y/PHH5/jjj8+MGTPSq1evpbMflspWAAAAAJZh22yzTS688MJ06dIlSdKxY8c8//zzSZJWrVqlXbt2WXPNNXPppZdmzJgx2X///bPpppumQ4cOGTBgQMaMGZNzzz03PXv2TJJ8+9vfziWXXJJJkyZl3Lhx843VoUOHPPnkk0mSKVOmZMqUKUmSESNG5IgjjsgZZ5yR9ddfv+YUtT333DO33nprJkyYkG233TbvvfdennvuufzpT3/KRRddlLPOOivz5s372vvATCIAAABgubf11ltn+PDhOfPMM5MkzZo1S8uWLfODH/wgSdK6desMGDAglZWVqaqqStu2bdO9e/cccsghOe644zJ27NjMmDEjhx9+eM02KyoqMnLkyBx44IEZO3ZsVl111STJjjvumMceeyx77bVX1lprrZrre/XqlUMPPTRt2rTJd77znXz44YdJkjXWWCMrr7xyNttsszRp0iSrrbZa3n///ey+++5ZaaWVMnDgwDRp8vUrnoriiysnNSC9e/fOddddV+4YAAAAQD2bOHFiNtpoo/+7YtasOj+R7CtZ2tsrg4MPPjjDhg3Luuuuu9iPWWC/ZtF9i9PNAAAAgIZlaRc6y3BBNGvWrPTu3TsbbrjhVyqIloTTzQAAAAAaqObNm5fsTCsziQAAAABQEgEAAACgJAIAAAAgSiIAAAAAoiQCAAAAGphZs0q7vQMOOCBPP/10kmTOnDnp2LFjLrnkkprb999//7zwwgtfacxtttnmK+dcHHvvvXcmT55cL9tWEgEAAAANSvPmSUXF0vtq3nzR43Xu3DmPPvpokuSxxx5L586dc8899yRJZs+enXfffTcbbrhhPT/r8mtS7gAAAAAA5bT11lvn/PPPz8CBA3Pvvfdmr732ytlnn53p06fnueeey5ZbbpkkueWWW3LZZZelUaNG6dixY4455phMnz49xx13XD788MMkyfDhw7PBBhvUbHvUqFGZPn16TjjhhFRUVNRcf84552TChAkpiiIDBgxI9+7dU1lZmQ033DAvv/xyZsyYkfPOOy9t27bN73//+9x33335zne+UzPOY489ljPOOCNNmjTJKquskrPPPjstWrT4WvtBSQTQwMyaVfdfOhbnPgAAwOL5wQ9+kFdffTVFUWTChAk56qijstVWW+XBBx/Miy++mC5duuSjjz7K6NGjc+2112bFFVfMsccemwceeCAPPvhgfvrTn6Zfv355/fXXM3To0Fx55ZVJkjPOOCMVFRU58cQT5xvv3nvvzeTJk3PVVVdl9uzZ2XvvvWtOT9tkk01y3HHH5fe//31uuummbLfddpkwYUKuueaafPLJJ9lpp52SJHfccUd+9rOf5cADD8xdd92Vjz/+WEkE8E3z+dTaRSmK0mQBAIDlQaNGjbLhhhtm3LhxWW211dKsWbN07do199xzT1544YUccMABefPNNzNt2rQcdNBBSZKZM2fmrbfeyksvvZSHH344t9xyS5Lk448/TpJ88MEHefHFF7POOussMN5LL72U5557LpWVlUmSefPm5Z133knyWWGVJN/5znfywQcfZNKkSdl4443TqFGjtGjRIuuvv36S5JBDDskFF1yQ/v37Z4011sgmm2zy9ffD194CAAAAwDJum222yYUXXpguXbokSTp27Jjnn38+SdKqVau0a9cua665Zi699NKMGTMm+++/fzbddNN06NAhAwYMyJgxY3LuueemZ8+eSZJvf/vbueSSSzJp0qSMGzduvrE6dOiQTp06ZcyYMfnLX/6S7t27p127dgvN1b59+zz99NOprq7OJ598kkmTJiVJbrzxxuyxxx4ZM2ZMvv/972fs2LFfex+YSQQAAAAs97beeusMHz48Z555ZpKkWbNmadmyZc3MntatW2fAgAGprKxMVVVV2rZtm+7du+eQQw7Jcccdl7Fjx2bGjBk5/PDDa7ZZUVGRkSNH5sADD8zYsWOz6qqrJkm23377PPLII+nXr18++eST7LjjjrWeKrbRRhtll112SZ8+fbL66qunTZs2SZIf/ehHGTJkSFZaaaU0bdo0v/vd7772PqgoioZ50kLv3r1z3XXXlTsGQFk43QwAgOXJxIkTs9FGG9VcXtprcC6va3p+eb8mi+5bnG4GAAAANChLu9BZHguiJaEkAgAAAEBJBAAAAICSCAAAAGgAGuiSycusJdmfSiIAAACgrJo3b56pU6cqipaSoigyderUNP+KizE1qac8AAAAAIulXbt2mTx5ct5///1yR/nGaN68edq1a/eVHqMkAgAAAMqqadOmad++fbljLPecbgYAAACAkggAAAAAJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAkHosiZ566qlUVlYmSaZOnZpBgwZlv/32S9++ffPmm2/W17AAAAAALIEm9bHRiy++ODfccENWXHHFJMlZZ52Vnj17pkePHnn44Yfz6quvZp111qmPoQEAAABYAvUyk2idddbJ6NGjay4//vjjmTJlSgYMGJAbb7wxW265ZX0MCwAAAMASqpeSaOedd06TJv83Sentt9/OKquskssuuyxrrrlmLr744voYFgAAAIAlVJKFq1u1apXtt98+SbL99tvn2WefLcWwAAAAACymkpREHTt2zL333pskmTBhQr73ve+VYlgAAAAAFlNJSqLBgwfn+uuvT9++fXPfffflkEMOKcWwAAAAACymevl0syRp165dxo4dmyRp27Zt/vznP9fXUAAAAAB8TSWZSQQAAABAw6YkAgAAAEBJBAAAAICSCAAAAIAoiQAAAACIkggAAACAKIkAAAAAiJIIAAAAgCiJAAAAAIiSCAAAAIAoiQAAAACIkgj4Jpg1a+ncBwAAYDnWpNwBAL625s2TiopF36coSpMFAABgGWUmEQAAAABKIgAAAACURAAAAABESQQAAABAlEQAAAAAREkEAAAAQJREAAAAAERJBAAAAECURAAAAABESQQAAABAlEQAAAAAREkELCdmzfp6twMAAHzTNSl3AIBSaN48qaio/faiKF0WAACAhshMIgAAAACUREAtnJ8FAACwXHG6GbBwzs8CAABYrphJBAAAAICSCAAAAAAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAkHosiZ566qlUVlbOd92NN96YffbZp76GBAAAAGAJNamPjV588cW54YYbsuKKK9ZcN3HixFxzzTUpiqI+hgQAAADga6iXmUTrrLNORo8eXXP5ww8/zNlnn51hw4bVx3AAAAAAfE31UhLtvPPOadLks0lKVVVVOe644zJs2LCsvPLK9TEcAAAAAF9TvS9c/dxzz+WNN97ISSedlKOOOiqTJk3KiBEj6ntYAAAAAL6CelmT6Is22WST3HTTTUmSyZMn56ijjspxxx1X38MCAAAA8BXU+0wiAAAAABq+eiuJ2rVrl7Fjx9Z5HQAAAADlZyYRAAAAAEoiAAAAAJREAAAAAERJBAAAAECURAAAAABESQQAAABAlEQAAAAAREkEAAAAQJREAAAAAERJBAAAAECURAAAAABESQQAAABAlEQAAAAAREkEAAAAQJREAAAAAERJBAAAAECURAAAAABESQQAAABAlEQAAAAAREkEAAAAQJREAAAAAERJBAAAAECURAAAAABESQQAAABAlEQAfA2zZi2d+wAAAOXXpNwBAFh2NW+eVFQs+j5FUZosAADA12MmEQAAAABKIgAAAACURAAAAABESQQAAABAlEQAAAAAREkEAAAAQJREAAAAAERJBAAAAECURAAAAABESQQAAABAlETAEpo1a+ncBwAAgIahSbkDAMum5s2TiopF36coSpMFAACAr89MIgAAAACURAAAAAAoiQAAAACIkoiFqWu1YasRAwAsn3xyBcA3moWrWVBdKxJbjRgAYPnkkysAvtHMJAIAAABASQQAAACAkggAAACAKIkAAAAAiJIIAAAAgCiJAAAAAIiSCAAAAIAoiaBBmTVr6dwHAAAAviolETQgzZsnFRWL/mrevNwpAaCB81cXAFgiTcodAAAAlqrP/+qyKEVRmiwAsAwxkwgAABowE6MAKJV6K4meeuqpVFZWJkkmTpyYfv36pbKyMgceeGA++OCD+hoWAAC+UZyODkCp1EtJdPHFF2f48OGZPXt2kmTEiBE5/vjjM2bMmPzsZz/LxRdfXB/DNlz+/AMAAAA0cPVSEq2zzjoZPXp0zeVRo0Zlo402SpJUVVVlhRVWqI9hGy5//gEAoDb+WAhAA1EvJdHOO++cJk3+b03s1VdfPUny+OOP5/LLL8+AAQPqY1gAAFj21PUHRQAokZJ9utnNN9+c//mf/8lFF12U1q1bl2pYAAAAABZDSUqi66+/Pn//+98zZsyYtGrVqhRDAgAAAPAV1HtJVFVVlREjRmTNNdfMr371qyTJFltskSOOOKK+hwYAAABgMdVbSdSuXbuMHTs2SfLII4/U1zAAAAAALAX1snA1sBA+uQQAAIAGrGQLV8Ny7/NPLlmUoihNFgAAAPgSM4kAAAAAUBIBALD8WZyzwJ0pDsDyRknUQPhFBQCgdD4/C3xRX82blzslAJSWkqiB8IsKANCg1fXXKn/NAoBlnoWrAQCoW10fwODDFwBgmWcmEQAAAABKIgAAYOlxZmL9sIYpUApKIgCWG964QP3xBpbP1bXWpnU2l4w1TIFSsCYRAMsNS6pA/anr+yvxPQYADZ2ZRAAA5WDqDQA0GA7LnzGTiG+8WbMWPfW2rtsBoF6YegMADYbD8mfMJOIbz3nxNCjLw58fAKAhMC0A4CszkwiglPyJAgBKwzEX4CszkwgAAAAAJREAAAAASiIA4JvEGiQALMvqOkY5hi0Z+22xWZMIAPjmsAYJAMuyuo5jjmFLxu8Hi81MIgAAAACURABAHUx9BwBYLjjdDABYNFPfAQCWC2YSAQAAAKAkAgAAAEBJBAAALKcWZ0k1y65BLXwDfSNZkwgAAFgu+VRs+Bp8A30jmUkEAABQbmZcAA2AkoivzKxCAABYyj6flVHbFyyD6npf6H1jw+N0M76yBjWrcNaszwIBAADQoNT13tHZaA2PkohlW4NqrAAAAGDZ5XQzAGpnDjAAACw3zCQCoHbmCAMAwHLDTCIAAAAAlEQAAAB8Q/loZvhKlEQAAAAsvmWpePn81PlFffm0ZKihJAIAaKCWpfdhwHJE8QLfWEoiACg17/xZTN6HAcuqug5jDnPQMPl0MwAotbo+NS7xyXEALNN8QCosm8wkAgAAAEBJBAAAwPLLWeDwf5REAMByxToZAHyR9d/g/1iTCABYrlgnAwBg4cwkAgAAAEBJBMA3hHOEAADga3G6GQDfDD5WHgAAvhYziQAAAABQEgEAAMCyYHHOrncGPl+H080AAABgGeDseuqbmUQAAAAAKIkAAAAAUBIBAAAAECURAAAAAFESAQAAABAlEQAAAACpx5LoqaeeSmVlZZLkjTfeyL777pt+/frlxBNPTHV1dX0NCwAAAMASqJeS6OKLL87w4cMze/bsJMlpp52W3/zmN/nb3/6Woihy55131sewAAAAACyheimJ1llnnYwePbrm8nPPPZctt9wySdK1a9c8+OCD9TEsAAAAAEuoXkqinXfeOU2aNKm5XBRFKioqkiQrr7xypk+fXh/DAgAAALCESrJwdaNG/zfMzJkzs8oqq5RiWAAAAAAWU0lKoh/84AcZP358kmTcuHH5yU9+UophAYASmDVr6dwHAIDyKklJNHjw4IwePTr77LNP5s6dm5133rkUwwIAJdC8eVJRseiv5s3LnRIAgLo0qfsuS6Zdu3YZO3ZskqR9+/a5/PLL62soAAAAAL6mkswkAgAAAKBhUxIBQANknR8AAEqt3k43AwCW3Ofr/CxKUZQmCwAAywcziQAAAABQEgEAAACgJAIAAAAgSiIAAAAA8hVKov/+97/1mQMAAACAMqrz080eeeSR/O53v0tVVVV22WWXrLXWWtlrr71KkQ0AAACAEqlzJtF5552Xyy+/PN/+9rdzyCGH5MorryxFLgAAAABKqM6SqFGjRmnVqlUqKiqywgorZOWVVy5FLgAAAABKqM6SaJ111sk555yTjz76KBdddFHWWmutUuQCAAAAoITqLIlOPPHErLXWWunYsWNWXHHFnHLKKaXIBQAAAEAJ1blw9SGHHJJLL720FFkAAAAAKJM6S6KWLVvmzjvvzHe/+900avTZxKP27dvXezAAAAAASqfOkmjatGm57LLLai5XVFTkr3/9a31mAgAAAKDE6iyJxowZM9/lOXPm1FsYAAAAAMqjzpLoqquuyp///OfMmzcvRVGkadOmue2220qRDQAAAIASqfPTzcaOHZsxY8aka9euOe2007LeeuuVIhcAAAAAJVRnSbTqqqtm9dVXz8yZM9OpU6f897//LUUuAAAAAEqozpKoZcuWueOOO1JRUZGrrroq06ZNK0UuAAAAAEqozpLo1FNPzVprrZWjjz46r7/+ek466aQSxAIAAACglGotia6++uokSYsWLbLRRhtl9dVXz5AhQ9KpU6eShQMAAACgNGotiW688caaf/fv378kYQAAAAAoj1pLoqIoFvpvAAAAAL55ai2JKioqFvpvAAAAAL55mtR2w6RJk3L00UenKIqaf3/unHPOKUk4AAAAAEqj1pLo3HPPrfl33759S5EFAAAAgDKptSTacsstS5kDAAAAgDKqdU0iAAAAAJYfSiIAAAAAaj/d7HMzZszIuHHjMmfOnJrrdt999/rMBAAAAECJ1VkSHXrooVl99dWz5pprJkkqKirqPRQAAAAApVVnSVQURc4+++xSZAEAAACgTOpck2iDDTbIU089lTlz5tR8AQAAAPDNUudMokceeSR33XVXzeWKiorceeed9RoKAAAAgNKqsyS64YYbSpEDAAAAgDKqsyS6884787e//S1z585NURT56KOPcuONN5YiGwAAAAAlUueaRH/6059y+OGHZ80118wee+yR9ddfvxS5AAAAACihOkuiVVddNT/+8Y+TJL17986UKVPqPRQAAAAApVVnSdS0adNMmDAh8+bNy3333Zf333+/FLkAAAAAKKE6S6KTTz458+bNy6BBgzJ27NgcccQRpcgFAAAAQAnVuXD1GmuskVdffTWPP/54DjvssLRv374UuQAAAAAooTpLolGjRuU///lPXnnllTRt2jQXXXRRRo0aVYpsAAAAAJRInaebPfbYYznzzDOz0korZY899sjkyZNLkQsAAACAEqqzJKqqqsrs2bNTUVGRqqqqNGpU50MAAAAAWMbUebpZ//7907t370ybNi177bVXBgwYUIJYAAAAAJRSnSVR9+7ds/XWW+eNN95Iu3bt0rp161LkAgAAAKCEai2Jhg4dWuuDTjvttHoJAwAAAEB51FoSPfvss5k1a1Z69eqVH//4xymKopS5AAAAACihWlehvvHGG/OnP/0ps2fPzkUXXZQnn3wy66yzTrp06VLKfAAAAACUwCLXJFp//fVzzDHHJEkmTJiQc845J//5z38yduzYkoQDAAAAoDTq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AAAAgCiJAAAAAIiSCAAAAIAoiQAAAACIkggAAACAKIkAAAAASNKkVAPNnTs3w4YNy9tvv505c+Zk0KBB2WGHHUo1PAAAAACLULKS6IYbbkirVq1y1lln5cMPP8wee+yhJAIAAABoIEpWEu2yyy7Zeeeday43bty4VEMDAAAAUIeSlUQrr7xykmTGjBk54ogj8pvf/KZUQwMAAABQh5IuXP3uu+/mgAMOyG677ZaePXuWcmgAAAAAFqFkM4k++OCDDBw4MCeccEK22mqrUg0LAAAAwGIo2UyiCy64IB9//HHOP//8VFZWprKyMrNmzSrV8AAAAAAsQslmEg0fPjzDhw8v1XAAAAAAfAUlXZMIAAAAgIZJSQQAAACAkggAAAAAJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAAURIBAAAAkKRJqQaqrq7OSSedlBdffDHNmjXLqaeemnXXXbdUwwMAAACwCCWbSXTHHXdkzpw5+fvf/56jjz46p59+eqmGBgAAAKAOJSuJHnvssXTp0iVJstlmm+XZZ58t1dAAAAAA1KFkJdGMGTPSokWLmsuNGzfOvHnzSjU8AAAAAItQURRFUYqBTjvttGy66abp0aNHkqRr164ZN25crffv1KlT2rZtW4poAAAAAMuFt99+O+PHj1/obSVbuHrzzTfP3XffnR49euTJJ5/M+uuvv8j71xYYAAAAgKWvZDOJPv90s5deeilFUWTkyJFZb731SjE0AAAAAHUoWUkEAAAAQMNVsoWrAQAAAGi4lEQAAAAAKIkAAAAAUBI1ONXV1TnhhBOyzz77pLKyMm+88Ua5I9XpqaeeSmVlZbljLNLcuXNz7LHHpl+/funTp0/uvPPOckdapKqqqgwdOjR9+/bNfvvtlzfffLPckeo0derUbLvttnnllVfKHaVOu+++eyorK1NZWZmhQ4eWO84iXXjhhdlnn33Su3fvXH311eWOU6vrrruuZp/uvffe+dGPfpSPP/643LFqNXfu3Bx99NHp27dv+vXr16Bft3PmzMnRRx+dvffeOwMHDszrr79e7kgL9cVjwRtvvJF99903/fr1y4knnpjq6uoyp1vQl49dt99+e44++ugyJqrdF7NOnDgx/fr1S2VlZQ488MB88MEHZU43vy9mnTRpUvbdd9/07ds3J510UqqqqsqcbkEL+x3mxhtvzD777FOmRLX7YtbnnnsuXbp0qfm5e/PNN5c53fy+mHXq1KkZNGhQ9ttvv/Tt27dB/k7zxbxHHnlkzX7dfvvtc+SRR5Y53fy+/PNg7733zr777puhQ4c2uJ+1X37N9unTJ/369cspp5zSoLIu7H1CQz2OLeo9zciRI3PllVeWMd2CFpa3oR7HFpZ1WTiO1YuCBuW2224rBg8eXBRFUTzxxBPFIYccUuZEi3bRRRcVu+66a7HXXnuVO8oiXXPNNcWpp55aFEVRTJs2rdh2223LG6gOt99+ezFkyJCiKIri4YcfbvCvgzlz5hSHHnposdNOOxWTJk0qd5xFmjVrVrHbbruVO8Ziefjhh4uDDz64qKqqKmbMmFH84Q9/KHekxXLSSScVV111VbljLNLtt99eHHHEEUVRFMX9999fHH744WVOVLsxY8YUw4cPL4qiKF555ZVi4MCBZU60oC8fCw4++ODi4YcfLoqiKI4//vji3//+dznjLeDLeU855ZRi5513Ln7zm9+UOdmCvpx1v/32K55//vmiKIriyiuvLEaOHFnOePP5ctZBgwYVjzzySFEURTF48OAG/zooiqJ4/vnniwMOOKDB/V7z5axjx44tLrnkkjKnWrgvZx08eHBx0003FUVRFA899FBx9913lzHdgmr7Xfajjz4qevXqVUyZMqVMyRb05ayHHnpocc899xRFURRHHXVUceedd5Yz3ny+nHWPPfYoHnvssaIoimLUqFHFP//5z3LGm8/C3ic01OPYwrJOnTq1OPDAA4sddtih+Nvf/lbmhPNbWN6GehxbWNaGfhyrL2YSNTCPPfZYunTpkiTZbLPN8uyzz5Y50aKts846GT16dLlj1GmXXXbJr3/965rLjRs3LmOauu2444455ZRTkiTvvPNOvv3tb5c50aKdccYZ6du3b1ZfffVyR6nTCy+8kE8//TQDBw7MAQcckCeffLLckWp1//33Z/31189hhx2WQw45JNttt125I9XpmWeeyaRJkxrkX+G/qH379qmqqkp1dXVmzJiRJk2alDtSrSZNmpSuXbsmSTp06NAgZz19+Vjw3HPPZcstt0ySdO3aNQ8++GC5oi3Ul/NuvvnmOemkk8oXaBG+nHXUqFHZaKONknw263SFFVYoV7QFfDnr6NGjs8UWW2TOnDl5//3306ZNmzKmW9CX83744Yc5++yzM2zYsDKmWrgvZ3322Wdzzz33ZL/99suwYcMyY8aMMqab35ezPv7445kyZUoGDBiQG2+8seZnQ0NR2++yo0ePzv7779+gfrf5ctaNNtooH330UYqiyMyZMxvUsezLWadMmZLNN988yWc/cx977LFyRVvAwt4nNNTj2MKyzpw5M7/61a+y2267lTHZwi0sb0M9ji0sa0M/jtUXJVEDM2PGjLRo0aLmcuPGjTNv3rwyJlq0nXfeuUEdkGqz8sorp0WLFpkxY0aOOOKI/OY3vyl3pDo1adIkgwcPzimnnJKdd9653HFqdd1116V169Y15WZD17x58xx44IG55JJLcvLJJ+eYY45psN9jH374YZ599tmcd955NVmLoih3rEW68MILc9hhh5U7Rp1WWmmlvP322+nevXuOP/74Bn3K7EYbbZS77747RVHkySefzJQpUxrcdOcvHwuKokhFRUWSz37+Tp8+vVzRFurLeXv06FGTt6H5ctbP37A+/vjjufzyyzNgwIAyJVvQl7M2btw4b7/9dnbdddd8+OGHad++fRnTLeiLeauqqnLcccdl2LBhWXnllcucbEFf3rebbLJJfvvb3+aKK67I2muvnT/96U9lTDe/L2d9++23s8oqq+Syyy7LmmuumYsvvriM6Ra0sN9lp06dmoceeii9e/cuU6qF+3LW7373uxkxYkS6d++eqVOnplOnTmVMN78vZ1177bXzyCOPJEnuvvvufPrpp+WKtoCFvU9oqMexhWVde+21s+mmm5Y72kItLG9DPY4tLGtDP47VFyVRA9OiRYvMnDmz5nJ1dfUyUcIsC959990ccMAB2W233dKzZ89yx1ksZ5xxRm677bYcf/zx+eSTT8odZ6GuvfbaPPjgg6msrMzEiRMzePDgvP/+++WOVav27dunV69eqaioSPv27dOqVasGm7dVq1bp3LlzmjVrlg4dOmSFFVbItGnTyh2rVh9//HFeffXV/PSnPy13lDpddtll6dy5c2677bZcf/31GTJkSGbPnl3uWAu15557pkWLFjnggANy991354c//GGDnw3ZqNH//Xoxc+bMrLLKKmVM881z880358QTT8xFF12U1q1blzvOIrVt2zb//ve/s+++++b0008vd5xaPffcc3njjTdy0kkn5aijjsqkSZMyYsSIcseq1c9+9rNsvPHGNf9+/vnny5yodq1atcr222+fJNl+++0b/Cz5JLn11luz6667NviftSNGjMgVV1yRW2+9NbvvvnuD/h4bOXJkLrzwwhx00EFp06ZNVl111XJHms+X3yc05OPYsvaeZmF5G+pxbGFZl5Xj2NKkJGpgNt9884wbNy5J8uSTT2b99dcvc6Jvhg8++CADBw7Msccemz59+pQ7Tp3++c9/5sILL0ySrLjiiqmoqGiwv6hcccUVufzyyzNmzJhstNFGOeOMM7LaaquVO1atrrnmmpof8FOmTMmMGTMabN6OHTvmvvvuS1EUmTJlSj799NO0atWq3LFqNWHChGy99dbljrFYVllllbRs2TJJ8q1vfSvz5s1rcLNzPvfMM8+kY8eOGTNmTHbcccesvfba5Y5Upx/84AcZP358kmTcuHH5yU9+UuZE3xzXX399zc/chv5aOOSQQ2oWWl955ZXne9PV0GyyySa56aabMmbMmIwaNSrf+973ctxxx5U7Vq0OPPDAPP3000mShx56KD/84Q/LnKh2HTt2zL333pvks+PE9773vTInqttDDz1Uc5pvQ/atb32r5gyE1VdfvUF/YMS9996bkSNH5qKLLspHH32UbbbZptyRaizsfUJDPY4ta+9pFpa3oR7HFpZ1WTqOLU2mqDQwP/vZz/LAAw+kb9++KYoiI0eOLHekb4QLLrggH3/8cc4///ycf/75SZKLL744zZs3L3Oyhdtpp50ydOjQ7Lfffpk3b16GDRvWYM7XXdb16dMnQ4cOzb777puKioqMHDmywc7W69atWyZMmJA+ffqkKIqccMIJDbYsTJLXXnst7dq1K3eMxTJgwIAMGzYs/fr1y9y5c3PkkUdmpZVWKneshVp33XVz3nnn5dJLL03Lli0b9OyGzw0ePDjHH398Ro0alQ4dOjToU2aXJVVVVRkxYkTWXHPN/OpXv0qSbLHFFjniiCPKnGzhDjrooAwZMiRNmzbNiiuumFNPPbXckb4xTjrppJxyyilp2rRpvv3tb9esY9gQDR48OMOHD89VV12VFi1a5Jxzzil3pDq99tprDerNa21OPfXUHHnkkWnSpEmaNm3aoF8H6667bg466KCsuOKK6dSpU7bddttyR6qxsPcJxx13XE499dQGdxxb1t7TfDlvVVVVXn755ay11loN7ji2sH37m9/8Zrk8jlUUDX2BCwAAAADq3fIxXwoAAACARVISAQAAAKAkAgAAAEBJBAAAAECURAAAAABESQQAsIDx48fnyCOPnO+6s88+O9ddd12ZEgEA1D8lEQAAAABpUu4AAADLktNPPz2PPfZYkmTXXXdN//79M2TIkPTo0SNdu3bNuHHjcvPNN+f0009Pt27d0qFDh3To0CFbbLFFLr744jRp0iRt27bNmWeemUaN/L0OAGg4lEQAAAvx8MMPp7KysubyW2+9lV/+8peZPHlyxo4dm3nz5qVfv3756U9/Wus23n333Vx33XVZddVVc8QRR2TAgAH5+c9/nn/+85+ZMWNGVllllVI8FQCAxaIkAgBYiJ/+9Kf5/e9/X3P57LPPzqxZs/KTn/wkFRUVadq0aTbddNO88sor8z2uKIqaf6+66qpZddVVkyRDhw7NhRdemCuvvDIdOnTIjjvuWJonAgCwmMxxBgBYTM2bN6851Wzu3Ll54oknsu6666ZZs2Z5//33kyTPP/98zf2/eDrZ3//+9/zqV7/K5ZdfniS5/fbbS5gcAKBuZhIBACymlVZaKe3atcs+++yTuXPnZpdddskPf/jD7LXXXhk2bFhuvPHGfPe7313oYzfZZJP84he/SKtWrbLyyitnu+22K2l2AIC6VBRfnBMNAAAAwHLJ6WYAAAAAKIkAAAAAUBIBAAAAECURAAAAAFESAQAAABAlEQAAAABREgEAAAAQJREAAAAASf4/iHtaMV4q3t4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# hours\n",
    "x = np.array(week_days_fare.hour)\n",
    "# an array of week day fare \n",
    "y = np.array(week_days_fare.amount)\n",
    "# an array of week end fare\n",
    "z = np.array(week_ends_fare.amount)\n",
    "\n",
    "# Set the figure size, title, x and y labels\n",
    "plt.figure(figsize = (20,10))\n",
    "plt.title('Mean Fare Amont For Each Hour - Weekdays Vs Weekends')\n",
    "plt.xlabel('Hours')\n",
    "plt.ylabel('Mean Fare')\n",
    "# Pass the three integers. The value of these integer should be less that 10\n",
    "ax=plt.subplot(1,1,1)\n",
    "ax.bar(x-0.2, y, width=0.2, color='red', align='center', label = 'Week days')\n",
    "ax.bar(x, z, width=0.2, color='blue', align='center', label = 'Week ends')\n",
    "plt.xticks(range(0,24))\n",
    "plt.legend()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We notice that the mean fares for each hour are different for week days and week ends. Mean fare for weekdays during morning hours 6,7 and 8 is lmuch ess compared to weekends."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Distribution'></a>\n",
    "### 4.2.3 Distribution of key numerical vairables"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will check the distribustion of 'travel_dist_km' and 'amount'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> We will check the distribution of the following variables: <br><br>\n",
    "                        1. 'amount' <br>\n",
    "                        2. 'travel_dist_km' <br>\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Distribution of fare 'amount'**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:39.974494Z",
     "start_time": "2022-01-26T20:30:38.459105Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJoAAAJZCAYAAADhxV+mAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABwTUlEQVR4nO3dd5xU5d3///eZvruzlbLShVUUNUoxligWjDF621HBlnirtzFqNCYxEgsaRdBo/Ea9o7cm+ktuNIJRoxJz241GYwNFBSvFRdoCW2Bnp585vz8WVsosLDBnZs6c1/PxyCM77Xw+15zZWfLOdV3HsCzLEgAAAAAAALCTPIVuAAAAAAAAAKWBoAkAAAAAAAA5QdAEAAAAAACAnCBoAgAAAAAAQE4QNAEAAAAAACAnCJoAAAAAAACQEwRNAABgm5YuXaoRI0bopJNO0kknnaQTTjhBEydO1D/+8Y+u59x111166qmntnqc//7v/9ZLL72U9bGNX7/HHnuopaVlu3r86KOPNHnyZEnSxx9/rMsvv3y7Xr8jTNPUj3/8Yx1zzDF6+OGHu+3nnXfe0fHHH79TtSKRiCZOnKj/+I//0AsvvLBTx3KKf/7zn7rrrrsK3QYAANgOvkI3AAAAnCEUCunpp5/uur1s2TKdd9558nq9OuaYY3TFFVds8xjvvPOOdtttt6yP9eT1W7NgwQI1NTVJkr71rW/p7rvv3qnj9URTU5PeeOMNzZ07V16vt9t+cuHTTz9Vc3OzXnzxxZwds9h9/PHHWrt2baHbAAAA24GgCQAA7JABAwbo8ssv14MPPqhjjjlGkyZN0u67764LLrhAd999t1588UX5/X7V1tZq2rRpevHFFzVv3jz95je/kdfr1csvv6y2tjZ9/fXXOuKII9Tc3Nz1ekn63e9+p48//liZTEY//elPdeSRR+rJJ5/U888/r/vvv1+Sum7feOONuvvuu9Xe3q5f/epXOvnkk3XzzTfr73//u9rb2/XrX/9an332mQzD0NixY/Wzn/1MPp9P3/rWt3TRRRfpzTff1KpVq3ThhRfqrLPO2mKss2fP1m9+8xvFYjH5/X799Kc/1ejRo3XhhRcqnU7r1FNP1T333KPBgwdLklasWLFFP9FoVFdeeaUWLVqkRCKhKVOmaP/991cymdQdd9yh9957T6Zpaq+99tJ1112ncDjcVX/RokW65ppr1NTUpJNOOkkzZ87Un/70J7388suKx+OKxWK6+uqrdfTRR+uee+7R3LlztWrVKu2xxx664447dN999+mFF15QJpPRgAEDdMMNN6i+vn6TMUajUd14441qbGxUW1ubKioqdMcdd2jYsGE699xztffee2vu3LlqaWnRGWecoTVr1ujdd99VLBbT7373O+2xxx5auXKlbrzxRi1btkyWZenkk0/WhRdeqKVLl+qEE07QBx98IEmb3H7yySf14osvyuPxqLGxUaFQSLfddpsikYhmzJgh0zRVWVmpK6+80pbPMQAAyC2WzgEAgB2255576osvvtjkvhUrVujPf/6znnjiCT355JM65JBD9NFHH+nss8/WPvvso1/+8pc6+uijJUnxeFzPPvusrrrqqi2OPXDgQP3tb3/T7bffrkmTJm11KV2/fv10+eWXa//999e0adM2eWzKlCmqqanRrFmz9MQTT+jzzz/XQw89JElKJpOqra3VjBkzdPfdd2vatGlKJBKbvL61tVWXX365rr32Ws2aNUu33XabrrrqKrW2tuqBBx7omum1IWTqrp+VK1fqvPPO09NPP62JEyfqnnvukSQ98MAD8nq9evLJJ/XMM8+ob9++uuOOOzbpYdiwYZoyZYoGDx6sp59+Ws3Nzfr3v/+t6dOna9asWbryyis3mcG1bNky/e1vf9Mdd9yhp556Sl988YX++te/6umnn9bhhx+u6667bov38PXXX1dVVZVmzpyp559/Xvvss48eeeSRTY45Y8YM3X777br99tt1wAEH6Mknn9TYsWO7lg3+4he/0IEHHqhZs2bp0Ucf1TPPPKNnn3222/O2wXvvvafrr79ef//737XffvvpgQce0H777aeJEyfquOOOI2QCAMBBmNEEAAB2mGEYCoVCm9xXX1+vPffcU6eccooOO+wwHXbYYTr44IOzvn7MmDHdHvvMM8+UJA0fPlwNDQ1ds2G21+uvv65HH31UhmEoEAho4sSJ+vOf/6yLLrpIknTUUUdJkvbee28lk0lFo1EFg8Gu13/00UcaPHiw9ttvP0nS7rvvrtGjR+vdd9/VgQce2OM+Bg0a1HWMPffcU0888YSkzn2I2tvb9e9//1uSlEql1KtXr60ea8CAAfrNb36jWbNmqbGxUR9++KE6Ojq6Hh85cqR8vs5/5r366qv6+OOPNX78eElSJpNRLBbb4pjf//73NWjQIE2fPl2NjY169913NWrUqK7HN4SDgwYNkiSNHTtWkjR48GC9++67ikajev/997tCvMrKSp166ql6/fXXu8bdnb333lu77LKLJGmvvfZy1fJAAABKDUETAADYYR9//LGGDx++yX0ej0cPP/ywPv74Y7311luaOnWqxo4dq1/+8pdbvL68vLzbY3s830y8zmQy8vl8MgxDlmV13Z9KpbbZYyaTkWEYm9xOp9NdtzeEShues/Hxpc4Nvzd+/YbnbHyMnvD7/V0/bzyOTCaja665RocffrgkqaOjY4tZVZubP3++LrnkEp133nk65JBD9O1vf1u//vWvux7f+H3NZDKbLAlMJpNZ9z36y1/+oscee0xnn322TjjhBNXU1Gjp0qVdjwcCgW7Hs6HO5u/dhvd6W+dt47By8+cCAABnYekcAADYIYsXL9a9996r888/f5P7P/vsMx1//PFqaGjQj370I5133nn6+OOPJUler7fHAc3f/vY3SZ2hypIlS7Tffvuprq5OX375pRKJhFKplJ5//vmu53d37EMPPVQPP/ywLMtSMpnUY489pu985zs9HufIkSO1aNEiffTRR5KkL7/8Uu+9954OOOCArb6up2M99NBD9cgjjyiZTCqTyej666/XnXfeudXXvPfee9pnn330n//5nzrggAP08ssvyzTNbo//+OOPKxKJSOq8ul+20O+NN97QKaecotNPP11Dhw7VK6+80u0xswmHw9pvv/26ltu1t7frqaee0ne+8x1VVVUplUppwYIFktSj5XTS9n1eAABAcWBGEwAA6JF4PK6TTjpJUudso2AwqJ/97Gc64ogjNnnennvuqWOPPVbjx49XeXm5QqFQ155A48aN05133tmjmUhff/21Tj75ZBmGoTvvvFM1NTVds3eOPfZY9enTRwceeKA+//xzSZ2B0O9//3tddtllOvfcc7uOc91112nKlCk64YQTlEqlNHbsWF188cU9HnddXZ3uuusu3XzzzYrH4zIMQ9OmTdPQoUM3mfGzue762dwll1yi2267TaeccopM09SIESM0adKkrfZ0/PHH64UXXtCxxx6rTCajI488UmvXru0KkzZ2+umnq6mpSWeccYYMw1C/fv106623bvG8888/X5MnT9bjjz/e1f/m+29tyx133KGbbrpJTz75pJLJ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e+6p66+/Xl6v15axdVfLrs+iJM2aNUsPP/ywZs6cKUm2jKu7Wnads+7+zW3H2LqrZcc5a25u1nXXXad169bJNE395je/0eDBg20ZV3e17BjXlVdeqTVr1kiSli1bpv3220//7//9P9u+87urZ8fYPv30U91www3yer3adddddcstt+T071lPatkxrvnz5+uGG25QIBDQiBEjdO2119r6d7q7ets9NgtF4/nnn7euvvpqy7Is64MPPrAuvvhi22rF43HrpJNOsu34lmVZDzzwgHX88cdbp59+umVZlvWjH/3Ievvtty3Lsqzrr7/eeuGFF2yr9dhjj1kPPvhgzo6/sccff9yaMmWKZVmW1dLSYh1++OG2jS1bLbvG9uKLL1qTJk2yLMuy3n77beviiy+29Zxlq2fneUsmk9Yll1xife9737MWLFhg69g2r2XXuLL9Hts1rmy17Dxfb7/9tvWjH/3IMk3TikQi1t13323b2LLVsnNsG9x4443WjBkzbP0sbl7LznG9+OKL1uWXX25ZlmW98cYb1mWXXWbb2LLVsmts06dPt6677jrLsixr4cKF1vnnn2/buLLVyvW4evK3edWqVdbxxx9vJRIJa926dV0/21XPsixr4sSJVnNzc07HdvPNN1vHHHOM9dOf/rTrOSeeeKLV2NhoZTIZ68ILL7TmzZtnW60777zTeu6553ZiRNlrnX322dYnn3xiWZZlPfroo9bUqVNzds56UsuycnO+stX78Y9/bL377ruWZVnW1VdfndPPY09q5Wpsm9eyLMv65JNPrB/84Add99k1rmy1LMu+c5btO8qusXX3fWjHObv66qutZ5991rIsy3rrrbesV1991bZxZatl17g2aGtrs0488USrqanJ1u/8bPUsy56xXXLJJdY///lPy7Is62c/+5n18ssv23bOstWya1ynnHKKNWfOHMuyOv+uPPXUU7aes2z1dmRsLJ0rInPmzNHYsWMlSSNHjtS8efNsq/XZZ58pFovp/PPP1w9+8APNnTs35zUGDx6se+65p+v2/Pnzu/6fvMMOO0z//ve/bas1b948/fOf/9TZZ5+ta665RpFIJGe1vv/97+uKK67ouu31em0bW7Zado3tu9/9rm6++WZJ0vLly9W7d29bz1m2enaet9tuu00TJ05U3759Jdn7edy8ll3jyvZ7bNe4stWy83y98cYbGj58uC699FJdfPHFOuKII2wbW7Zado5Nkj7++GMtWLBAEyZMsPWzuHktO8c1dOhQmaapTCajSCQin89n29iy1bJrbAsWLNBhhx0mSRo2bJgWLlxo27iy1cr1uHryt/mjjz7SqFGjFAgEVFlZqcGDB+uzzz6zrV4mk1FjY6MmT56siRMn6vHHH89JrdGjR+vGG2/suh2JRJRMJjV48GAZhqFDDz1Ub731li21pM6xPvHEEzrrrLN06623Kp1O56TWnXfeqREjRkjqnB0cDAZzds56UitX5ytbvXvuuUff/va3lUwmtXr1avXq1cu2sWWrZddnsbW1VXfccYeuueaarvvsGle2Wnaes2zfUXaNLVstu87Z+++/r6amJp133nmaNWuWDjjgANvGla2WXePa4J577tE555yjvn372vqdn62eXWMbMWKE2traZFmWOjo65PP5bDtn2WrZNa6mpiaNHj1aUuffmjlz5th6zrLV25GxETQVkUgkonA43HXb6/Xu8D9KtiUUCumCCy7Qgw8+qF//+tf6xS9+kfNaxxxzjHy+b1ZnWpYlwzAkSRUVFWpvb7et1r777qtf/vKXeuSRRzRo0CD9/ve/z1mtiooKhcNhRSIRXX755frpT39q29iy1bJzbD6fT1dffbVuvvlmHXPMMbaes2z17Brbk08+qbq6uq4gV7Lv85itll3jyvZ7bNe4stXae++9bfsstra2at68ebrrrrtsH1u2Wnb+nkmdS/UuvfRSSfZ+N25ey85xlZeXa9myZTr22GN1/fXX69xzz7VtbNlq2TW2ESNG6NVXX5VlWZo7d66amppsG1e2Wvvss09Ox9WTv82RSGST6fAVFRU7HHD1pF40GtU555yj22+/XX/84x/1l7/8ZYf+wbx5reOOO66rlrTlv7N25txtq5YkHXLIIbr++uv1yCOPKBqNasaMGTmpteH/xHj//ff18MMP67zzzsvZOetJrVydr2z1vF6vli1bpuOPP16tra0aOnSobWPLVsuOz6Jpmrr22mt1zTXXdC05kWTLuLqrZec5y/bda9c5y1bLru+PZcuWqaqqSn/605/Ur18//eEPf7BtXNlq2TUuqXN7h7feekunnnqqpNx9Fntaz66xbVjCduyxx6q5uVkHHnigbecsWy27xjVo0CC9++67kqRXX31VsVjM1nOWrd6OjI2gqYiEw2F1dHR03c5kMlv8oubK0KFDdeKJJ8owDA0dOlQ1NTVavXq1LbU22Hj/io6ODlVVVdlW6+ijj9Y+++zT9fMnn3yS0+OvWLFCP/jBD3TSSSfphBNOsHVsm9eye2y33Xabnn/+eV1//fVKJBJd99t1zjaud+ihh9oytieeeEL//ve/de655+rTTz/V1VdfrZaWlq7Hczm2bLUOO+wwW8aV7fe4ubm56/FcjitbrbFjx9r2WaypqdGhhx6qQCCgYcOGKRgMbvI/CHM5tmy1jjjiCNvGtm7dOi1atEgHHXSQJHu/GzevZef3x5/+9Ccdeuihev755/X0009r0qRJSqVSXY/ncmzZatn1ezZ+/HiFw2H94Ac/0Kuvvqq9997btnOWrdYxxxxj63d+trFs/u+Rjo6OHd7LpSf1ysrK9IMf/EBlZWUKh8M66KCDdvh/BG9NtnHZ+W+R8ePHa9CgQTIMQ0cddVROz90//vEP3XDDDXrggQdUV1dn6znbvJbd52vAgAF64YUXdOaZZ+rWW2+1dWyb17JjbPPnz1djY6NuvPFG/exnP9OCBQt0yy232DKu7mrZec6y/V2x65xlq2XX2GpqajRu3DhJ0rhx4zRv3jzbxpWtlp3n7LnnntPxxx8vr9crKft3Y65+x7LVs2tst9xyix555BE999xzOvnkk239/shWy65xTZ06Vffff78uuugi9erVS7W1tbaes2z1dmRsBE1FZPTo0Xr99dcldW5WOXz4cNtqPf7447r11lsldU6Pi0Qi6tOnj231JGmvvfbSO++8I0l6/fXXtf/++9tW64ILLtBHH30kSXrrrbe099575+zYa9as0fnnn6+rrrpKp512miT7xpatll1je+qpp3T//fdL6vwDYBiG9tlnH9vOWbZ6l112mS1je+SRR/Twww9r+vTpGjFihG677TYddthhtowtW61LLrnElnFl+z0+5JBDbBlXtlqXXnqpbb9nY8aM0b/+9S9ZlqWmpibFYjEdfPDBtowtW62LLrrItrG99957+s53vtN1287vxs1r2fndWFVV1fWPnOrqaqXTadvGlq3WxRdfbMvYPv74Y40ZM0bTp0/Xd7/7XQ0aNMi2cWWrZec5k7J//vbdd1/NmTNHiURC7e3tWrhwYc7+TZKt3ldffaWzzjpLpmkqlUrp/fffz/k4pc7/MeX3+7VkyRJZlqU33njDtn+LWJalE088UStXrpSU23P39NNPd/2dGTRokCTZds6y1bLzfF188cX66quvJHX+P/Qej8e2sWWrZcfY9t13Xz377LOaPn267rzzTu2222669tprbRlXd7XsPGfZvqPsOmfZatk1tjFjxui1116T1Pm3dLfddrNtXNlq2XnO3nrrra5l2pJ93x/d1bNrbNXV1V2zVvv27at169bZNrZstewa12uvvaapU6fqgQceUFtbmw455BBbz1m2ejsyNq46V0SOPvpovfnmm5o4caIsy9LUqVNtq3XaaafpV7/6lc4880wZhqGpU6faNntqg6uvvlrXX3+97rzzTg0bNkzHHHOMbbVuvPFG3XzzzfL7/erdu3fXXkC58D//8z9at26d7r33Xt17772SpGuvvVZTpkzJ+diy1Zo0aZKmTp2a87F973vf069+9SudffbZSqfTuuaaa9TQ0GDbOctWr1+/fradt82Vwucx2+9xbW2tLePKVisYDNp2vo488ki99957Ou2002RZliZPnqyBAwfaMrZsterq6mwb2+LFizVw4MCu23Z+FjevZed343nnnadrrrlGZ511llKplK688krts88+towtW61hw4bZMrYhQ4borrvu0kMPPaTKykrdcsstikajtowrW601a9bY+r2Y7fPn9Xp17rnn6qyzzpJlWbryyisVDAZtrXfCCSfojDPOkN/v10knnaTdd989J/U2t2F5rGmaOvTQQ7XffvvZUscwDE2ZMkWXXXaZQqGQGhoadMYZZ+z0cU3T1C233KJ+/frpJz/5iSTp29/+ti6//PKcn7Ot1bLrfF100UWaNGmS/H6/ysrKNGXKFPXp08eWz2O2Wn379s3bZ9GucWXT0NBg27iy/V0Jh8O2jK27WnaM7eqrr9Z1112nGTNmKBwO67e//a2qq6ttGVd3tew6Z4sXL+4KjiX7P4ub17Pr8zhlyhRdeeWV8vl88vv9uvnmm20bW7ZaAwcOtGVcQ4YM0UUXXaSysjIdeOCBOvzwwyXJtnPWXb3tHZthWZaVk44AAAAAAADgaiydAwAAAAAAQE4QNAEAAAAAACAnCJoAAAAAAACQEwRNAAAAAAAAyAmCJgAAAAAAAOSEvdezBwAAKEJLly7ViSeeqL333rvrvgMPPFCXXXZZzmrccMMN+vDDD/XUU0/l7Jg9sXz5cn322WcaN25cXusCAABIBE0AAMCldtttN02fPt2WY8diMb3//vsaPny43nnnHR144IG21Mnm7bff1qJFiwiaAABAQRA0AQAArGeapiZPnqyVK1eqtbVVhx12mH76059q0qRJamtrU1tbm+6//3798Y9/1HvvvSfLsnTeeefp2GOP3eQ4//d//6eDDz5Yhx12mB555JGuoOmEE07Q/vvvry+++EJDhw5Vr169NHv2bAUCAT3wwAOKxWK66qqrFIlEZJqmrrjiCh188MEaN26c/u///k/BYFB33HGHhg0bpgEDBugPf/iD/H6/li5dquOOO04XXXSRHnjgAcXjcY0aNUpHHXVUId5GAADgYgRNAADAlRYsWKBzzz236/Ydd9yhVCqlkSNH6vTTT1cikegKmiTpoIMO0nnnnafXXntNS5cu1YwZM5RIJHTGGWfokEMOUVVVVdex/vrXv+qmm25SQ0ODbrzxRjU1Nam+vl4dHR06/vjjNWbMGH3/+9/Xr371K1155ZU655xztGDBAj3zzDP6zne+ox/+8IdqamrSmWeeqZdeeqnbMSxfvlzPPPOMksmkxo4dqx//+Me66KKLtGjRIkImAABQEARNAADAlbItnYtEIvr444/19ttvKxwOK5lMdj02dOhQSdIXX3yh+fPnd4VU6XRay5cv7wqaFi5cqC+//FK33nqrJMkwDD366KNdgdWGfaGqqqrU0NDQ9XMikdDChQt1wgknSJLq6+sVDofV0tKySY+WZXX9PHz4cPl8Pvl8PoVCoZy8LwAAADuDq84BAACs9+STT6qyslK//e1vdf755ysej3cFO4ZhSJKGDRumAw88UNOnT9ef//xnHXvssRo4cGDXMf7617/qyiuv1IMPPqgHH3xQf/7zn/XEE090hVYbjpNNQ0ODZs+eLUlqamrSunXrVFNTo0AgoFWrVsmyLH322Wddz892LI/Ho0wms/NvBgAAwA5gRhMAAMB6Bx98sH72s59pzpw5Kisr05AhQ7Rq1apNnjNu3Di9++67OuussxSNRvXd735X4XBYkpRMJvXss8/q6aef7np+//79teeee+r555/fZv0f/ehHuuaaa/T8888rHo/rpptuks/n04UXXqiLLrpIAwYM2GSJXjbDhw/Xfffdp7333lv/8R//sQPvAgAAwI4zrI3nXwMAAAAAAAA7iKVzAAAAAAAAyAmCJgAAAAAAAOQEQRMAAAAAAABygqAJAAAAAAAAOUHQBAAAAAAAgJwgaAIAAAAAAEBOEDQBAAAAAAAgJwiaAAAAAAAAkBP/P58UpYsE3lsqAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20,10))\n",
    "sns.set_style(\"darkgrid\")\n",
    "plt.title(\"Distribution of the fare amount\")\n",
    "plt.xlabel(\"Fare Amount\")\n",
    "plt.ylabel(\"Frequency\")\n",
    "plt.xlim(-10,20)\n",
    "plt.xticks(range(0,200,5))\n",
    "\n",
    "snsplot = sns.kdeplot(df_taxi.amount, shade=True)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see that most the trips have a fare amount of 2 to 20 dollars. There are a few small peaks around 50 and 58 dollars as well."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Distribustion of the travel distance in km**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:41.134013Z",
     "start_time": "2022-01-26T20:30:39.974494Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJIAAAJZCAYAAADyEh9SAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABfnElEQVR4nO39eZikZXk37n9q6wV6mBlkEYVBHEBQoggu8RVccEF9VRBQBxE04IIG10TBBUQZFo0bEk0k0Z95wQQVtxj9qqAmRqKIKLKJCiIQhGHYhO6eqepafn+0tCw9QzNTT1U1fZ7H4XFMd3XVdd/1dPeMH677ekqdTqcTAAAAALgf5X4vAAAAAID5QZAEAAAAwJwIkgAAAACYE0ESAAAAAHMiSAIAAABgTgRJAAAAAMyJIAkAuF//+7//m1133TX77bdf9ttvv7zoRS/KihUr8q1vfWvma0499dR87WtfW+/r/P3f/33OPffcWR+7+/Mf9ahH5dZbb31Aa7z44otz3HHHJUkuueSSvPnNb35Az98QrVYrb3jDG7LvvvvmzDPPXOd6zj///LzwhS/cqFrXXXdd3vSmN8362KpVq7JixYqNev0PfOADOe2005Ikr33ta3PllVeu9+sPP/zwB3yNAID5r9rvBQAA88PIyEi+/vWvz3x8/fXX59WvfnUqlUr23XffvOUtb7nf1zj//POz4447zvrYXJ6/PldeeWVWrVqVJPmLv/iLfOITn9io15uLVatW5Uc/+lEuuuiiVCqVda6nG/7whz/k6quvnvWxrbfeOmeddVbXav3TP/3T/X7Neeed17V6AMD8IUgCADbIwx/+8Lz5zW/OZz7zmey777455phjstNOO+WII47IJz7xiZxzzjmp1WpZunRpTj755Jxzzjm59NJL86EPfSiVSiXf+973cvvtt+e6667LM57xjNxyyy0zz0+Sj3/847nkkkvSbrfz1re+Nc985jPzla98Jd/5znfy6U9/OklmPj7++OPziU98InfeeWfe9a53Zf/9988JJ5yQ//iP/8idd96Z97///bniiitSKpWy99575+1vf3uq1Wr+4i/+Iq973ety3nnn5aabbsprXvOavOIVr7jPXn/2s5/lQx/6UNasWZNarZa3vvWt2WOPPfKa17wmzWYzBxxwQE477bQsW7YsSXLDDTfcZz2Tk5N529velt/97nep1+tZuXJlnvCEJ6TRaOTDH/5wLrjggrRarTz60Y/Oe9/73oyNjc3Ub7Vaee9735tVq1bliCOOyPvf//4ccsghWb58ea6//vqccsopOfzww/OLX/wip512Wq655prceOONWb16dXbZZZeceOKJ93i9JBkfH8973vOeXHHFFdlqq61SqVSy5557Jkn22WefnHrqqXnkIx+Zd73rXbnmmmtSLpfzmMc8Jh/4wAfynve8J0nyqle9KqeffnquuOKKfPrTn06j0citt96a/fffP29961tz/vnn52Mf+1i22267/Pa3v02z2cz73//+7LnnnpmYmMjKlSvz85//PJVKJc9+9rPztre9LVNTU/f7fgAA/eNoGwCwwXbZZZf85je/ucfnbrjhhvzLv/xLvvzlL+crX/lKnvrUp+biiy/OIYcckt122y3vfOc785znPCdJsnbt2nzzm9/MO97xjvu89rbbbpuvfvWr+bu/+7scc8wx6z1Gtc022+TNb35znvCEJ+Tkk0++x2MrV67MkiVL8o1vfCNf/vKX8+tf/zqf/exnkySNRiNLly7NWWedlU984hM5+eSTU6/X7/H82267LW9+85vznve8J9/4xjfywQ9+MO94xzty22235fTTT5/p1LorRFrXem688ca8+tWvzte//vWsWLFi5hjZ6aefnkqlkq985Sv593//92y11Vb58Ic/fI81VCqVrFy5MsuWLctnPvOZmdd74xvfmO985zvZcsst7/H1F1xwQT7+8Y/n//v//r9Uq9V88pOfvM979olPfCIjIyP59re/nVNPPXXWbqdzzjknExMT+frXv56zzz47yfQRu7v29C//8i956EMfms9+9rM55ZRT8pWvfCVf+MIXcvrpp89cr4svvjiHH354vva1r+WAAw7Ixz72sZn69Xo93/rWt/K1r30tP//5z/PTn/50Tu8HANA/giQAYIOVSqWMjIzc43Nbb711dtlll7zkJS/JBz/4wey666559rOfPevz7+qAmc3BBx+cJNl5552zfPny/OIXv9igNf7whz/MK1/5ypRKpQwNDWXFihX54Q9/OPP4s571rCTJYx7zmDQajUxOTt7j+RdffHGWLVuWxz3ucUmSnXbaKXvssUd++tOfPqB1bLfddjOvscsuu8wELf/5n/+Z73//+9l///2z33775dxzz81VV111v69XrVaz++67z/rY8573vGyxxRYpl8s56KCD8qMf/eg+X/PjH/84+++/f0qlUjbffPOZcO/u9txzz1x55ZU59NBDc/rpp+dVr3pVtt9++3t8TalUyj/+4z/msssuy9///d/nlFNOSafTyZo1a5IkD3vYw7LrrrsmSR796Efnj3/8Y5Lkf/7nf3LQQQelUqlkaGgoZ555Zp785Cdv8PsBAPSGo20AwAa75JJLsvPOO9/jc+VyOWeeeWYuueSS/PjHP85JJ52UvffeO+985zvv8/xNNtlkna9dLv/5v3e12+1Uq9WUSqV0Op2Zz09NTd3vGtvtdkql0j0+bjabMx8PDw8nyczX3P31k+ljZXd//l1fc/fXmItarTbz57vvo91u593vfnee/vSnJ0kmJibu0xU1m6GhoVSrs/9T7u7zmtrt9j3ey7u7+17vPeMpmQ6/zjnnnJx//vn5yU9+kr/6q7/KBz7wgeyzzz4zXzM5OZmXvOQlefazn50nPOEJOfDAA3PuuefOvPbdg8a77/uu63mXG264ISMjIxv8fgAAvaEjCQDYIFdffXU+9alP5fDDD7/H56+44oq88IUvzPLly/P6178+r371q3PJJZckmQ4r5hrAfPWrX02SXHbZZbn22mvzuMc9Lptvvnl++9vfpl6vZ2pqKt/5zndmvn5dr73XXnvlzDPPTKfTSaPRyBe/+MX8n//zf+a8z9133z2/+93vcvHFFydJfvvb3+aCCy7Ik570pPU+b6573WuvvfL5z38+jUYj7XY7xx57bD760Y/O+npzCc6S5Hvf+17uvPPOtNvtfPGLX8wzn/nM+3zN3nvvnbPPPjvtdjt//OMf873vfe8+X/Ov//qvede73pW99tor73jHO7LXXnvl8ssvv8f+rrnmmoyPj+etb31r9tlnn5x//vkze1mfpzzlKfnqV7+adrudRqORN7/5zbngggvm/H4AAP2hIwkAmJO1a9dmv/32SzLdLTQ8PJy3v/3tecYznnGPr9tll13y/Oc/PwceeGA22WSTjIyM5L3vfW+S6SHOH/3oR+cUiFx33XUzR68++tGPZsmSJXnqU5+aJz7xiXn+85+fLbfcMk9+8pPz61//Osl04PPJT34yRx11VA499NCZ13nve9+blStX5kUvelGmpqay995758gjj5zzvjfffPOceuqpOeGEE7J27dqUSqWc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b36TE088MaeeemqRa1uQ1k61UutCR1K1UkpDRxIAAADQRXM62vaWt7wlv/3tb/PiF784f/d3f5ett946SXLAAQfkLW95S6ELXGi615FUTl1HEgAAANBFcwqSXvayl2X33XfPpptumptuumnm8//2b/9W2MIWqnqzix1JgiQAAACgi+bU+vKLX/wip512WpJk5cqVOf3005Mkw8PDxa1sgao32125a1ut7GgbAAAA0F1zSiy+//3v55hjjkmSfOITn8j3v//9Qhe1kE0fbetCR5KjbQAAAECXzSlIKpVKaTQaSZKpqal0Op1CF7WQ1ZvtVLswI6li2DYAAADQZXOakbRixYq86EUvys4775zf/e53ec1rXlP0uhasRrOVoS50JNXKJR1JAAAAQFfNKUh66Utfmmc961m57rrrst1222XzzTcvel0L1tqpdqrdmJFUESQBAAAA3TWnIOlXv/pVvvCFL6Rer8987uSTTy5sUQtZo9WdGUm1ihlJAAAAQHfNKUg65phj8spXvjIPfehDi17PgtdotjPUhRlJ1XIpk41WF1YEAAAAMG1OQdIWW2yRl770pUWvZcHrdDppNNuplnUkAQAAAINnTkHSwx/+8Jx++unZddddUypNhxx77bVXoQtbiKZanVTKpZS7EiS5axsAAADQXXMKkqampnL11Vfn6quvnvmcIKn7Gq12hqobf6wt0ZEEAAAAdN+cgqSTTz45V199da699to86lGPylZbbVX0uhakepfmIyXTM5J0JAEAAADdNKcg6cwzz8w555yTP/7xj3nJS16Sa665Jscdd1zRa1tw6k0dSQAAAMDgmlNq8c1vfjOf+9znsmjRorzqVa/KL3/5y6LXtSA1mu3UutSRVKuU0hAkAQAAAF00p9Si0+kkycyg7aGhoeJWtIDVuzkjydE2AAAAoMvmdLTthS98YQ455JD84Q9/yGtf+9o8+9nPLnpdC1Kj2c5QZePv2JYk1Uo5jWanK68FAAAAkMwxSHrlK1+ZpzzlKfnNb36THXbYIbvsskvR61qQ6t0+2qYjCQAAAOiiOQVJf//3fz/z56uuuirnnntujjrqqMIWtVDVW+3UutSRVCuXBUkAAABAV80pSNpiiy2STM9Kuvzyy9NuCyiK0O1h21OCJAAAAKCL5hQkrVix4h4fv+Y1rylkMQtdd4+2mZEEAAAAdNec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/GGS5KKLLsrOO+8889jy5ctzzTXX5Pbbb0+j0cjPfvazPP7xj1/vcwAAAADov1Kn0+l0+0XvugPbb37zm3Q6nZx00km5/PLLMzk5mZe//OUzd23rdDo58MADc8ghh8z6nOXLl3d7aQAAAABsoEKCJAAAAAAefNyLHgAAAIA5ESQBAAAAMCeCJAAAAADmpNrvBTDtrmHjv/71rzM0NJSVK1dm++23L6TW/vvvn0WLFiVJtt1225x88sldr/HLX/4yH/7wh3PGGWfkmmuuyTHHHJNSqZSddtop73vf+1IudyfDvHudyy67LEceeWQe8YhHJEkOPvjgvOAFL9joGlNTU3n3u9+d66+/Po1GI294wxuy4447dn1Ps9V56EMfWsieWq1W3vve9+bqq69OpVLJySefnE6nU8h1mq3WnXfeWci+kuSWW27JAQcckM9+9rOpVquFfe/du9batWsL2dO9f16PPPLIwvZ071qvfOUrC7tOn/70p/P9738/U1NTOfjgg/OkJz2pkH3du86jH/3oQvb0la98JV/96leTJPV6Pb/61a/yr//6rznppJO6uqfZ6px11lmF/e475phjcv3116dcLueEE04o5GdqtjpF/Tw1Go28613vynXXXZexsbEcd9xxKZVKhXzvzVZrYmKiq/uay9+1X/ziF3PWWWelWq3mDW94Q575zGcWVmvlypX5+c9/nk033TRJ8qlPfWrmd8qG1kqSc845J9/+9rfzkY98JMn03X1PPPHEVCqV7LXXXjnqqKM2ek+z1fnud7+bD33oQ9lmm22SJG9605vypCc9aaPq/OpXv8oJJ5yQSqWSoaGhfPCDH8wWW2xRyHVaV60irtOVV16ZY489Np1OJ7vsskuOPfbYVCqVruxrLnWK+t5Lkm984xs588wz84UvfCFJur6nddUpYk/r+rdyt/e0rjpF7OmWW27Je9/73txxxx1ptVr50Ic+lGXLlhXyM7WuWt3Y193rvO1tb8vNN9+cJLn++uvzuMc9Lh/72McK2dO6anV7T7/61a/yvve9L5VKJY94xCNy4oknFvZ31LpqdXtPl112Wd73vvdlaGgou+66a97znvcUtqd11erWz9QG6TAQvvOd73SOPvroTqfT6fziF7/oHHnkkYXUWbt2bWe//fYr5LXvcvrpp3de+MIXdl760pd2Op1O5/Wvf33nJz/5SafT6XSOPfbYzne/+91C6nzxi1/sfOYzn+nKa9/d2Wef3Vm5cmWn0+l0br311s7Tn/70QvY0W52i9nTOOed0jjnmmE6n0+n85Cc/6Rx55JGFXafZahW1r0aj0XnjG9/Yee5zn9u58sorC9vTbLWK2NNsP69F7Wm2WkVdp5/85Ced17/+9Z1Wq9UZHx/vfOITnyhkX7PVKWpPd3f88cd3zjrrrEK//+5ep8jfE29+85s7nU6n86Mf/ahz1FFHFbKn2eoUtaczzjij8973vrfT6XQ6V111Vefwww8v7DrNVqub+5rL37U33XRT54UvfGGnXq937rjjjpk/F1Gr0+l0VqxY0bnlllu6uq8TTjihs++++3be+ta3znzNi1/84s4111zTabfbnde85jWdSy+9tJA6H/3oRzvf/va3u7qfQw45pHP55Zd3Op1O59/+7d86J510UmHXabZanU4x1+kNb3hD56c//Wmn0+l0jj766K59/82lTlF76nQ6ncsvv7xz2GGHzXyuiD3NVqeoPc32O6iIPa3rd10Rezr66KM73/zmNzudTqfz4x//uPODH/ygsJ+p2Wp1Y1+zfU90Op3O7bff3nnxi1/cWbVqVWF7mq1WEXt64xvf2PnP//zPTqfT6bz97W/vfO973ytsT7PVKmJPL3nJSzoXXnhhp9OZ/vvia1/7WmF7mq1WN/a0MRxtGxAXXnhh9t577yTJ7rvvnksvvbSQOldccUXWrFmTww8/PIcddlguuuiirtdYtmxZTjvttJmPL7vsspn/gve0pz0t//M//1NInUsvvTT/+Z//mUMOOSTvfve7Mz4+3pU6z3ve8/KWt7xl5uNKpVLInmarU9Senv3sZ+eEE05IkvzhD3/IFltsUdh1mq1WUfv64Ac/mBUrVmSrrbZKUtz33my1itjTbD+vRe1ptlpFXacf/ehH2XnnnfPXf/3XOfLII/OMZzyjkH3NVqeoPd3lkksuyZVXXpmXv/zlhX7/3b1OUXvaYYcd0mq10m63Mz4+nmq1WsieZqtT1J6uvPLKPO1pT0uSPPKRj8xVV11V2HWarVY39zWXv2svvvjiPP7xj8/Q0FAWLVqUZcuW5YorriikVrvdzjXXXJPjjjsuK1asyNlnn92Vfe2xxx45/vjjZz4eHx9Po9HIsmXLUiqVstdee+XHP/5x1+sk0/v88pe/nFe84hU55ZRT0mw2N7rORz/60ey6665Jpjt2h4eHC7tOs9Uq6jqddtppeeITn5hGo5HVq1fnIQ95SFf2NZc6Re3ptttuy4c//OG8+93vnvlcEXuarU5Re5rtd1ARe5qtTlF7+vnPf55Vq1bl1a9+db7xjW/kSU96UmE/U7PV6sa+7l3nLqeddlpe+cpXZquttipsT7PVKmJPu+66a26//fZ0Op1MTEykWq0WtqfZahWxp1WrVmWPPfZIMv13yIUXXljYnmar1a2fqQ0lSBoQ4+PjGRsbm/m4Uqls0D9Y7s/IyEiOOOKIfOYzn8n73//+/O3f/m3X6+y7776pVv98arLT6aRUKiVJNt1009x5552F1HnsYx+bd77znfn85z+f7bbbLp/85Ce7UmfTTTfN2NhYxsfH8+Y3vzlvfetbC9nTbHWK2lOSVKvVHH300TnhhBOy7777FnadZqtVxL6+8pWvZPPNN58JZJPivvdmq1XEnmb7eS1qT7PVesxjHlPI999tt92WSy+9NKeeemqh+5qtTpE/U8n0Ubq//uu/TlLc99+96xS1p0022STXX399nv/85+fYY4/NoYceWsieZqtT1J523XXX/OAHP0in08lFF12UVatWFXadZqu12267dW1fc/m7dnx8/B4t7ptuuukGhVdzqTU5OZlXvvKV+bu/+7v88z//c/71X/91g/7xfO9aL3jBC2ZqJff999KGXrP7q5MkT33qU3Psscfm85//fCYnJ3PWWWdtdJ27/uPDz3/+85x55pl59atfXdh1mq1WUdepUqnk+uuvzwtf+MLcdttt2WGHHbqyr7nUKWJPrVYr73nPe/Lud7975shIkq7vaV11irpOs/1uLeI6zVanqD1df/312WyzzfK5z30u22yzTf7pn/6psJ+p2Wp1Y1/3rpNMj0/48Y9/nAMOOCBJd7735lqriD3ddcTs+c9/fm655ZY8+clPLmxPs9UqYk/bbbddfvrTnyZJfvCDH2TNmjWF7Wm2Wt36mdpQgqQBMTY2lomJiZmP2+32fX7Iu2GHHXbIi1/84pRKpeywww5ZsmRJVq9e3fU6d3f3WRMTExPZbLPNCqnznOc8J7vtttvMny+//PKuvfYNN9yQww47LPvtt19e9KIXFbane9cpck/JdFfNd77znRx77LGp1+szny/iOt291l577dX1fX35y1/O//zP/+TQQw/Nr371qxx99NG59dZbZx7v5p5mq/W0pz2t63ua7ef1lltumXm8m3uardbee+9dyPffkiVLstdee2VoaCiPfOQjMzw8fI//I9itfc1W5xnPeEZhP1N33HFHfve73+Uv//IvkxT3u+/edYr6PfG5z30ue+21V77zne/k61//eo455phMTU3NPN6tPc1Wp4ifpyQ58MADMzY2lsMOOyw/+MEP8pjHPKaw6zRbrX333bew77/Z9nHvf1tMTEx0ZXbCbLVGR0dz2GGHZXR0NGNjY/nLv/zLQv5BO9ueivp3xYEHHpjtttsupVIpz3rWs7p2vb71rW/lfe97X04//fRsvvnmhV2n2WoVeZ0e/vCH57vf/W4OPvjgnHLKKYXt6951itjTZZddlmuuuSbHH3983v72t+fKK6/MiSee2PU9ratOUddptr8virhOs9Upak9LlizJPvvskyTZZ599cumllxb2vTdbraL29e1vfzsvfOELU6lUksz+u69bvyfuXauIPZ144on5/Oc/n29/+9vZf//9C/0dMVutIvZ00kkn5dOf/nRe97rX5SEPeUiWLl1a2J5mq9Wrv3fXRZA0IPbYY4/88Ic/TDI9RHLnnXcupM7ZZ5+dU045Jcl0i9z4+Hi23HLLQmrd5dGPfnTOP//8JMkPf/jDPOEJTyikzhFHHJGLL744SfLjH/84j3nMY7ryujfffHMOP/zwvOMd78hBBx2UpJg9zVanqD197Wtfy6c//ekk039ZlEql7LbbboVcp9lqHXXUUV3f1+c///mceeaZOeOMM7Lrrrvmgx/8YJ72tKcVsqfZar3xjW/s+p5m+3l96lOfWsieZqv113/914V8/+2555757//+73Q6naxatSpr1qzJU57ylK7va7Y6r3vd6wrZU5JccMEF+T//5//MfFzU77571ynq98Rmm20284+fxYsXp9lsFrKn2eoceeSRhezpkksuyZ577pkzzjgjz372s7PddtsVdp1mq1XUtUpm/3577GMfmwsvvDD1ej133nlnrrrqqq78+2K2Wr///e/zile8Iq1WK1NTU/n5z3/e1f3dZWxsLLVaLddee206nU5+9KMfFfLvik6nkxe/+MW58cYbk3Tven3961+f+ftju+22S5LCrtNstYq6TkceeWR+//vfJ5n+L/DlcrmQfc1Wp4g9Pfaxj803v/nNnHHGGfnoRz+aHXfcMe95z3u6vqd11SnqOs32O6iI6zRbnaL2tOeee+a//uu/kkz//bjjjjsW9jM1W62i9vXjH/945nh0UtzvidlqFbGnxYsXz3STbrXVVrnjjjsK29NstYrY03/913/lpJNOyumnn57bb789T33qUwvb02y1evX37rq4a9uAeM5znpPzzjsvK1asSKfTyUknnVRInYMOOijvete7cvDBB6dUKuWkk04qpPPp7o4++ugce+yx+ehHP5pHPvKR2XfffQupc/zxx+eEE05IrVbLFltsMTOXZ2P94z/+Y+6444586lOfyqc+9akkyXve856sXLmyq3uarc4xxxyTk046qet7eu5zn5t3vetdOeSQQ9JsNvPud787y5cvL+Q6zVZrm222KeRa3VuvvveSYr7/Zvt5Xbp0aSF7mq3W8PBwIdfpmc98Zi644IIcdNBB6XQ6Oe6447Ltttt2fV+z1dl8880L+967+uqrs+222858XNT3373rFPW779WvfnXe/e535xWveEWmpqbytre9LbvttlvX9zRbnUc+8pGF7Gn77bfPqaeems9+9rNZtGhRTjzxxExOThZynWardfPNNxf2/Tfb91ulUsmhhx6aV7ziFel0Onnb296W4eHhwmq96EUvyste9rLUarXst99+2Wmnnbqws/u666hqq9XKXnvtlcc97nFdr1EqlbJy5cocddRRGRkZyfLly/Oyl71so16z1WrlxBNPzDbbbJM3velNSZInPvGJefOb39z167S+WkVcp9e97nU55phjUqvVMjo6mpUrV2bLLbfs+r5mq7PVVlv17HuviD3NZvny5YXsaba/L8bGxrq+p3XVKWJPRx99dN773vfmrLPOytjYWD7ykY9k8eLFhf3um61WEfu6+uqrZwLgpNjvvXvXKuL7b+XKlXnb296WarWaWq2WE044obA9zVZr22237fqett9++7zuda/L6OhonvzkJ+fpT396khSyp3XV6tXvvtmUOp1Op2fVAAAAAJi3HG0DAAAAYE4ESQAAAADMiSAJAAAAgDkRJAEAAAAwJ4IkAAAAAOZEkAQALCjnn39+nvKUp+TQQw/NK1/5yqxYsSLf+ta38qtf/Sp///d/v87nXXDBBbniiisKXVuj0cg73vGOtNvtHHroobnqqquSJBMTE3nlK1+Z008/fU6vc+qpp+bKK68scqkAwAIlSAIAFpy//Mu/zBlnnJEzzzwzn/nMZ/LP//zPSZKjjjpqnc/58pe/nJtuuqnQdX3uc5/L85///JTLf/4n2vj4eF7zmtfk+c9/fl73utfN6XX+6q/+Kh/60IeKWiYAsIBV+70AAIB+2nTTTfPyl788H/jAB/LQhz40H/vYx3LMMcfk2muvTb1ezxFHHJFly5blv//7v3PZZZdlxx13zPe///1897vfTbPZzKJFi3LaaaflP/7jP/Jf//VfWbt2ba699tq89rWvzQEHHJBf/vKXOfHEE9PpdLL11lvnwx/+cK655pqsXLkySbJkyZKcdNJJGRsby7//+7/nq1/96sza7rzzzhxzzDF5xStekZe85CVJpjuqTj/99NRqtdx4441ZsWJFfvKTn+SKK67IYYcdlle84hXZbLPNMjw8nCuuuCK77LJLX95XAODBSZAEACx4D3nIQ3LbbbfloQ99aMbHx3P++efny1/+cpLkvPPOy2677Za99947L3jBC/LQhz40t99+ez73uc+lXC7niCOOyCWXXJJkunvoM5/5TH7/+9/nyCOPzAEHHJBjjz02H/vYx7J8+fJ8/vOfz1VXXZX3v//9Oemkk7LjjjvmS1/6Uv75n/85+++/f8bGxlKr1WbW9Y53vCNbbLFFVq1adY/13njjjfna176Wyy67LG95y1tyzjnnZNWqVTnqqKPyile8IknyqEc9Kj/96U8FSQBAVwmSAIAF7w9/+ENe/OIX57e//W3GxsZy7LHH5thjj834+Hhe/OIX3+Nry+VyarVa3v72t2eTTTbJjTfemGazmSQzoc0222yTRqORJLnllluyfPnyJMkhhxySJDNhUpJMTU1lhx12yG233ZYtttjiHrX+5m/+JnvttVcOPPDA7LHHHnnSk56UJNlpp51Sq9WyaNGiLFu2LENDQ1m8eHHq9frMc7fccsv7BFAAABtLkAQALGjj4+P50pe+NBPy3HTTTbnsssvyyU9+MvV6PU9/+tOz3377pVQqpdPp5Iorrsi5556bL33pS1mzZk0OOOCAdDqdJEmpVLrP62+11Vb5/e9/n0c84hE5/fTTs8MOO2SHHXbIBz/4wTzsYQ/LhRdemNWrV+chD3lI7rjjjns8d6eddsrY2Fg++MEP5q1vfetMl9Rsde7tj3/8Yx7ykIds7NsDAHAPgiQAYMH5yU9+kkMPPTTlcjmtVitvetObsnjx4px//vnZcssts3r16uy///7ZZJNNcvjhh6dareZxj3tcPvzhD+ejH/1oRkdHc8ABB2RoaChbbrnleodwv//978+73/3ulMvlbLnllnn1q1+dbbbZJkcffXRarVaS5MQTT8z222+fW2+9Nc1mM9XqPf+Jtvvuu+dlL3tZ/uZv/iavf/3r57THiy++OG9729s2/E0CAJhFqXPXf0IDAKCvPv3pT+eRj3xknvOc52zU69x+++055phj8o//+I9dWhkAwLTy/X8JAAC98KpXvSrf/va30263N+p1Pve5z+lGAgAKoSMJAAAAgDnRkQQAAADAnAiSAAAAAJgTQRIAAAAAcyJIAgAAAGBOBEkAAAAAzIkgCQAAAIA5+f8D4iVlXwbbrcsAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (20,10))\n",
    "sns.style = ('darkgrid')\n",
    "plt.title(\"Distribution of the trip distance\")\n",
    "plt.xlabel(\"Distance(Km)\")\n",
    "plt.ylabel(\"Frequency\")\n",
    "plt.xlim(-10, 200)\n",
    "plt.xticks(range(0,200,5))\n",
    "\n",
    "sns.plot = sns.kdeplot(df_taxi[df_taxi.travel_dist_km<600].travel_dist_km, shade=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see that most the trips have a travel distance of 2.5 km to 25 km. There are a few instances of 0 km as well."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>We have generated new features, removed redundant features and removed the outliers.\n",
    "<br>                    \n",
    "We now progress to build the model.\n",
    "</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='Random_Forest'></a>\n",
    "# 5.  Random Forest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is an example of the `Bagging` technique. It constructs multiple decision trees on randomly selected data samples. We can use the bootstrap sampling method to select the random samples of the same size from the dataset to construct multiple trees."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='RF_Model'></a>\n",
    "## 5.1 Random Forest Model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this section we build a model using random forest regressor."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>In order to build the model, we do the following: <br><br>\n",
    "                       1. Split the features and target into seperate data frames<br>\n",
    "                       2. Split the data into training and test sets<br>\n",
    "                       3. Build model<br>\n",
    "                       4. Predict the values using test set <br>\n",
    "                       5. Compute accuracy measures <br>\n",
    "                       6. Tabulate the results\n",
    "</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Split the data into features and target dataframes**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Store the amount variable which is the target variable, into y."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:41.149970Z",
     "start_time": "2022-01-26T20:30:41.139997Z"
    }
   },
   "outputs": [],
   "source": [
    "# select only the target variable 'amount' and store it in dataframe 'y'\n",
    "y = pd.DataFrame(df_taxi['amount'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, use this 'y' as a target variable to build the classification models."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:41.273188Z",
     "start_time": "2022-01-26T20:30:41.156952Z"
    }
   },
   "outputs": [],
   "source": [
    "# use 'drop()' to remove the variable 'amount' from df_taxi\n",
    "# 'axis = 1' drops the corresponding column(s)\n",
    "X = df_taxi.drop('amount',axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:41.415389Z",
     "start_time": "2022-01-26T20:30:41.275177Z"
    },
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>longitude_of_pickup</th>\n",
       "      <th>latitude_of_pickup</th>\n",
       "      <th>longitude_of_dropoff</th>\n",
       "      <th>latitude_of_dropoff</th>\n",
       "      <th>no_of_passenger</th>\n",
       "      <th>hour</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>dayofweek</th>\n",
       "      <th>travel_dist_km</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-73.844311</td>\n",
       "      <td>40.721319</td>\n",
       "      <td>-73.841610</td>\n",
       "      <td>40.712278</td>\n",
       "      <td>1</td>\n",
       "      <td>17</td>\n",
       "      <td>15</td>\n",
       "      <td>6</td>\n",
       "      <td>2009</td>\n",
       "      <td>0</td>\n",
       "      <td>1.030764</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-74.016048</td>\n",
       "      <td>40.711303</td>\n",
       "      <td>-73.979268</td>\n",
       "      <td>40.782004</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2010</td>\n",
       "      <td>1</td>\n",
       "      <td>8.450134</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-73.982738</td>\n",
       "      <td>40.761270</td>\n",
       "      <td>-73.991242</td>\n",
       "      <td>40.750562</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>18</td>\n",
       "      <td>8</td>\n",
       "      <td>2011</td>\n",
       "      <td>3</td>\n",
       "      <td>1.389525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-73.987130</td>\n",
       "      <td>40.733143</td>\n",
       "      <td>-73.991567</td>\n",
       "      <td>40.758092</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>21</td>\n",
       "      <td>4</td>\n",
       "      <td>2012</td>\n",
       "      <td>5</td>\n",
       "      <td>2.799270</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>-73.968095</td>\n",
       "      <td>40.768008</td>\n",
       "      <td>-73.956655</td>\n",
       "      <td>40.783762</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>2010</td>\n",
       "      <td>1</td>\n",
       "      <td>1.999157</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   longitude_of_pickup  latitude_of_pickup  longitude_of_dropoff  \\\n",
       "0           -73.844311           40.721319            -73.841610   \n",
       "1           -74.016048           40.711303            -73.979268   \n",
       "2           -73.982738           40.761270            -73.991242   \n",
       "3           -73.987130           40.733143            -73.991567   \n",
       "4           -73.968095           40.768008            -73.956655   \n",
       "\n",
       "   latitude_of_dropoff  no_of_passenger  hour  day  month  year  dayofweek  \\\n",
       "0            40.712278                1    17   15      6  2009          0   \n",
       "1            40.782004                1    16    5      1  2010          1   \n",
       "2            40.750562                2     0   18      8  2011          3   \n",
       "3            40.758092                1     4   21      4  2012          5   \n",
       "4            40.783762                1     7    9      3  2010          1   \n",
       "\n",
       "   travel_dist_km  \n",
       "0        1.030764  \n",
       "1        8.450134  \n",
       "2        1.389525  \n",
       "3        2.799270  \n",
       "4        1.999157  "
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use this 'X' as a set of predictors to build the model."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Split the data into training and test sets**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:30:41.780089Z",
     "start_time": "2022-01-26T20:30:41.418159Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The shape of X_train is: (34992, 11)\n",
      "The shape of X_test is: (14997, 11)\n",
      "The shape of y_train is: (34992, 1)\n",
      "The shape of y_test is: (14997, 1)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# split data into train subset and test subset for predictor and target variables\n",
    "# 'test_size' returns the proportion of data to be included in the test set\n",
    "# set 'random_state' to generate the same dataset each time you run the code \n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)\n",
    "\n",
    "# check the dimensions of the train & test subset for \n",
    "# print dimension of predictors train set\n",
    "print(\"The shape of X_train is:\",X_train.shape)\n",
    "\n",
    "# print dimension of predictors test set\n",
    "print(\"The shape of X_test is:\",X_test.shape)\n",
    "\n",
    "# print dimension of target train set\n",
    "print(\"The shape of y_train is:\",y_train.shape)\n",
    "\n",
    "# print dimension of target test set\n",
    "print(\"The shape of y_test is:\",y_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Build model using RandomForestRegressor**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:31:14.803390Z",
     "start_time": "2022-01-26T20:30:41.780089Z"
    },
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestRegressor(random_state=10)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#intantiate the regressor\n",
    "rf_reg = RandomForestRegressor(n_estimators=100, random_state=10)\n",
    "\n",
    "# fit the regressor with training dataset\n",
    "rf_reg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**3. Predict the values using test set**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:31:15.360618Z",
     "start_time": "2022-01-26T20:31:14.805170Z"
    }
   },
   "outputs": [],
   "source": [
    "# predict the values on test dataset using predict()\n",
    "y_pred = rf_reg.predict(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**4. Compute accuracy measures**\n",
    "\n",
    "Now we calculate accuray measures Root-mean-square-error (RMSE), R-squared and Adjusted R-squared."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:31:15.383446Z",
     "start_time": "2022-01-26T20:31:15.360618Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error (MAE): 2.06849660066934\n",
      "Mean Squared Error (MSE): 19.606631425668667\n",
      "Root Mean Squared Error (RMSE): 4.427937604084848\n"
     ]
    }
   ],
   "source": [
    "# Calculate MAE\n",
    "rf_reg_MAE = metrics.mean_absolute_error(y_test, y_pred)\n",
    "print('Mean Absolute Error (MAE):', rf_reg_MAE)\n",
    "\n",
    "# Calculate MSE\n",
    "rf_reg_MSE = metrics.mean_squared_error(y_test, y_pred)\n",
    "print('Mean Squared Error (MSE):', rf_reg_MSE)\n",
    "\n",
    "# Calculate RMSE\n",
    "rf_reg_RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred))\n",
    "print('Root Mean Squared Error (RMSE):', rf_reg_RMSE)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**5. Tabulate the results**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:31:15.563210Z",
     "start_time": "2022-01-26T20:31:15.383446Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MAE</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Random Forest</td>\n",
       "      <td>2.068497</td>\n",
       "      <td>19.606631</td>\n",
       "      <td>4.427938</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Model      MAE       MSE     RMSE\n",
       "0  Random Forest  2.068497 19.606631 4.427938"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create the result table for all accuracy scores\n",
    "# accuracy measures considered for model comparision are RMSE\n",
    "# create a list of column names\n",
    "cols = ['Model', 'MAE', 'MSE', 'RMSE']\n",
    "\n",
    "# create a empty dataframe of the colums\n",
    "# columns: specifies the columns to be selected\n",
    "result_tabulation = pd.DataFrame(columns = cols)\n",
    "\n",
    "# compile the required information\n",
    "rf_reg_metrics = pd.Series({'Model': \"Random Forest \",\n",
    "                     'MAE':rf_reg_MAE,\n",
    "                     'MSE': rf_reg_MSE,\n",
    "                     'RMSE': rf_reg_RMSE     \n",
    "                   })\n",
    "\n",
    "# append our result table using append()\n",
    "# ignore_index=True: does not use the index labels\n",
    "# python can only append a Series if ignore_index=True or if the Series has a name\n",
    "result_tabulation = result_tabulation.append(rf_reg_metrics, ignore_index = True)\n",
    "\n",
    "# print the result table\n",
    "result_tabulation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b>Let us also take a look at building a random forest model with grid search.\n",
    "</b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='RF_CV'></a>\n",
    "## 5.2 Random Forest with GridSearchCV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we show how a decision tree is optimized by cross-validation, which is done using the `GridSearchCV()` from sklearn library.\n",
    "\n",
    "The performance of the selected hyperparameters and trained model is then measured on the test set that was not used during the model building."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"todo.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> Now we build a random forest using the GridSearchCV. We start with our original data set gradually proceeding with our analysis<br><br>\n",
    "                        To build a Random Forest using GridSearchCV, we do the following:<br>\n",
    "                        1. Use GridSearch to obtain the optimal values of hyperparameters <br>\n",
    "                        2. Build the model using the hyperparameters obtained in step 1<br>\n",
    "                        3. Do predictions on the test set<br>\n",
    "                        4. Compute accuracy measures <br>\n",
    "                        5. Tabulate the results <br>                     \n",
    "                      </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**1. Use GridSearch to obtain the optimal values of hyperparameters**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:31:15.670982Z",
     "start_time": "2022-01-26T20:31:15.563210Z"
    }
   },
   "outputs": [],
   "source": [
    "# create a dictionary with hyperparameters and its values\n",
    "# pass the n_estimators \n",
    "# pass the list of values to 'min_samples_split' that assigns minimum number of samples to split an internal node\n",
    "# pass the list of values to 'max_depth' that assigns maximum depth of the tree\n",
    "# pass the list of values to 'min_samples_leaf' that assigns minimum number of samples required at the terminal/leaf node\n",
    "# pass the list of values to 'max_leaf_nodes' that assigns maximum number of leaf nodes in the tree\n",
    "tuned_paramaters = [{'n_estimators': [ 85, 100],\n",
    "                     'min_samples_split': [15,20],\n",
    "                     'max_depth': [8, 10]\n",
    "                     #'min_samples_leaf': [5,10],\n",
    "                     #'max_leaf_nodes': [10, 15]\n",
    "                    }]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:48:42.849264Z",
     "start_time": "2022-01-26T20:31:15.670982Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best parameters for random forest regressor:  {'max_depth': 10, 'min_samples_split': 20, 'n_estimators': 85} \n",
      "\n"
     ]
    }
   ],
   "source": [
    "# instantiate the 'RandomForestRegressor' \n",
    "# pass the 'random_state' to obtain the same samples for each time you run the code\n",
    "rf_reg_CV= RandomForestRegressor(random_state = 10)\n",
    "\n",
    "# use GridSearchCV() to find the optimal value of the hyperparameters\n",
    "# n_estimator: pass the decision tree classifier model\n",
    "# param_grid: pass the list 'tuned_parameters'\n",
    "# cv: number of folds in k-fold i.e. here cv = 10\n",
    "grid = GridSearchCV(estimator = rf_reg_CV, \n",
    "                         param_grid = tuned_paramaters, \n",
    "                         cv = 10)\n",
    "\n",
    "# fit the model on X_train and y_train using fit()\n",
    "dt_grid = grid.fit(X_train, y_train)\n",
    "\n",
    "# get the best parameters\n",
    "print('Best parameters for random forest regressor: ', dt_grid.best_params_, '\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**2. Build the model using the hyperparameters obtained in step 1**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:48:58.169387Z",
     "start_time": "2022-01-26T20:48:42.849264Z"
    }
   },
   "outputs": [],
   "source": [
    "# instantiate the 'RandomForestRegressor'\n",
    "# 'best_params_' returns the dictionary containing best parameter values and parameter name  \n",
    "# 'get()' returns the value of specified parameter\n",
    "# pass the 'random_state' to obtain the same samples for each time you run the code\n",
    "dt_grid_model = RandomForestRegressor(n_estimators = dt_grid.best_params_.get('n_estimators'),\n",
    "                                       max_depth = dt_grid.best_params_.get('max_depth'),\n",
    "                                       #max_leaf_nodes = dt_grid.best_params_.get('max_leaf_nodes'),\n",
    "                                       #min_samples_leaf = dt_grid.best_params_.get('min_samples_leaf'),\n",
    "                                       min_samples_split = dt_grid.best_params_.get('min_samples_split'),\n",
    "                                       random_state = 10)\n",
    "\n",
    "# use fit() to fit the model on the train set\n",
    "dt_grid_model = dt_grid_model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**3. Predict the values using test set**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:48:58.396513Z",
     "start_time": "2022-01-26T20:48:58.169387Z"
    }
   },
   "outputs": [],
   "source": [
    "# predict the class labels using 'X_test'\n",
    "y_pred = dt_grid_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**4. Compute accuracy measures**\n",
    "\n",
    "Now we calculate accuray measures Root-mean-square-error (RMSE), R-squared and Adjusted R-squared."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:48:58.427441Z",
     "start_time": "2022-01-26T20:48:58.401508Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error (MAE): 2.108015582329935\n",
      "Mean Squared Error (MSE): 19.952915628853532\n",
      "Root Mean Squared Error (RMSE): 4.466868660354089\n"
     ]
    }
   ],
   "source": [
    "# calculate MAE\n",
    "rf_reg_CV_MAE = metrics.mean_absolute_error(y_test, y_pred)\n",
    "print('Mean Absolute Error (MAE):', rf_reg_CV_MAE)\n",
    "                                         \n",
    "# calculate MSE\n",
    "rf_reg_CV_MSE = metrics.mean_squared_error(y_test, y_pred)\n",
    "print('Mean Squared Error (MSE):', rf_reg_CV_MSE)\n",
    "                                         \n",
    "# calculate RMSE\n",
    "rf_reg_CV_RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred))\n",
    "print('Root Mean Squared Error (RMSE):', rf_reg_CV_RMSE)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**5. Tabulate the results**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2022-01-26T20:48:58.632040Z",
     "start_time": "2022-01-26T20:48:58.430432Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>MAE</th>\n",
       "      <th>MSE</th>\n",
       "      <th>RMSE</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Random Forest</td>\n",
       "      <td>2.068497</td>\n",
       "      <td>19.606631</td>\n",
       "      <td>4.427938</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Random Forest with Grid Search</td>\n",
       "      <td>2.108016</td>\n",
       "      <td>19.952916</td>\n",
       "      <td>4.466869</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             Model      MAE       MSE     RMSE\n",
       "0                   Random Forest  2.068497 19.606631 4.427938\n",
       "1  Random Forest with Grid Search  2.108016 19.952916 4.466869"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create the result table for all accuracy scores\n",
    "# accuracy measures considered for model comparision are MAE, MSE, RMSE\n",
    "# create a list of column names\n",
    "#cols = ['Model', 'MAE', 'MSE', 'RMSE']\n",
    "\n",
    "# create a empty dataframe of the colums\n",
    "# columns: specifies the columns to be selected\n",
    "#result_tabulation = pd.DataFrame(columns = cols)\n",
    "\n",
    "# compile the required information\n",
    "rf_reg_metrics = pd.Series({'Model': \"Random Forest with Grid Search \",\n",
    "                     'MAE':rf_reg_CV_MAE,\n",
    "                     'MSE': rf_reg_CV_MSE,\n",
    "                     'RMSE': rf_reg_CV_RMSE     \n",
    "                   })\n",
    "\n",
    "# append our result table using append()\n",
    "# ignore_index=True: does not use the index labels\n",
    "# python can only append a Series if ignore_index=True or if the Series has a name\n",
    "result_tabulation = result_tabulation.append(rf_reg_metrics, ignore_index = True)\n",
    "\n",
    "# print the result table\n",
    "result_tabulation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"conclusion\"> </a>\n",
    "# 6. Conclusion and Interpretation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table align=\"left\">\n",
    "    <tr>\n",
    "        <td width=\"8%\">\n",
    "            <img src=\"infer.png\">\n",
    "        </td>\n",
    "        <td>\n",
    "            <div align=\"left\", style=\"font-size:120%\">\n",
    "                <font color=\"#21618C\">\n",
    "                    <b> The regression algorithms named in the above table have been implemented on the given dataset. The performance of the models were evaluated using MAE, MSE,RMSE. <br><br>\n",
    "                        The above result shows that the RMSE value for both the model is much less than the standard deviation of the 'amount' (target) variable. Both the models have performed well. We can further fine tune the model for various hyperparameter values.\n",
    "                    </b>\n",
    "                </font>\n",
    "            </div>\n",
    "        </td>\n",
    "    </tr>\n",
    "</table>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": false,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}