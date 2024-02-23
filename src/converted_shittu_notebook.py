{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "9b900594",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "2051a03a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('C://Users//USER//Documents//shittu_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "e5d74acb",
   "metadata": {
    "scrolled": false
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
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>18393</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>20228</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>18857</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>17623</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>17474</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0  18393       2     168    62.0    110     80            1     1      0   \n",
       "1   1  20228       1     156    85.0    140     90            3     1      0   \n",
       "2   2  18857       1     165    64.0    130     70            3     1      0   \n",
       "3   3  17623       2     169    82.0    150    100            1     1      0   \n",
       "4   4  17474       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio  \n",
       "0     0       1       0  \n",
       "1     0       1       1  \n",
       "2     0       0       1  \n",
       "3     0       1       1  \n",
       "4     0       0       0  "
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "c540af64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(70000, 13)"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "45cf80be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id             0\n",
       "age            0\n",
       "gender         0\n",
       "height         0\n",
       "weight         0\n",
       "ap_hi          0\n",
       "ap_lo          0\n",
       "cholesterol    0\n",
       "gluc           0\n",
       "smoke          0\n",
       "alco           0\n",
       "active         0\n",
       "cardio         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "7271894f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_diabetic(row):\n",
    "    if row['cholesterol'] == 3 or row['gluc'] == 3:\n",
    "        return 3  # Diabetic\n",
    "    elif row['gluc'] == 2:\n",
    "        return 2  # Prediabetic\n",
    "    else:\n",
    "        return 1  # Non-diabetic\n",
    "\n",
    "# Apply the function to derive diabetic status\n",
    "df['diabetic'] = df.apply(derive_diabetic, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "9a04a2f0",
   "metadata": {},
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
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>diabetic</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>18393</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>20228</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>18857</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>17623</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>17474</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0  18393       2     168    62.0    110     80            1     1      0   \n",
       "1   1  20228       1     156    85.0    140     90            3     1      0   \n",
       "2   2  18857       1     165    64.0    130     70            3     1      0   \n",
       "3   3  17623       2     169    82.0    150    100            1     1      0   \n",
       "4   4  17474       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio  diabetic  \n",
       "0     0       1       0         1  \n",
       "1     0       1       1         3  \n",
       "2     0       0       1         3  \n",
       "3     0       1       1         1  \n",
       "4     0       0       0         1  "
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "31e7c396",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo',\n",
       "       'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'diabetic'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "9a66d65c",
   "metadata": {},
   "outputs": [],
   "source": [
    "newdata =df[['cholesterol','gluc', 'diabetic']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "777f49d3",
   "metadata": {},
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
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>diabetic</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>cholesterol</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.451578</td>\n",
       "      <td>0.777446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gluc</th>\n",
       "      <td>0.451578</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.749860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>diabetic</th>\n",
       "      <td>0.777446</td>\n",
       "      <td>0.749860</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             cholesterol      gluc  diabetic\n",
       "cholesterol     1.000000  0.451578  0.777446\n",
       "gluc            0.451578  1.000000  0.749860\n",
       "diabetic        0.777446  0.749860  1.000000"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newdata.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "e8e00f92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(newdata.corr(),annot=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "adf38860",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('shittu_datanew.csv', index= False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b8d5785",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
