
# coding: utf-8

# # Explorando datos de Pokémon con Pandas

# ![](http://pre02.deviantart.net/b8ea/th/pre/f/2011/201/c/2/c29adebe114379d32e11919f7ed86224-d412swy.jpg)

# # Importar librerías

# In[5]:


import pandas as pd


# # Cargar datos para crear un DataFrame

# In[8]:


data = pd.read_csv('pokemon.csv', index_col='#')


# ## La unidad canónica de pandas es el DataFrame, que se parece a un spreadsheet en Excel. Tiene filas y columnas nombradas. Es muy fácil e intuitivo manipular.

# In[9]:


ls 


# # Echar un vistazo a las primeras filas

# In[10]:


data.head()


# # Trabajando con un Pandas "Series"

# In[11]:


type(data['Name'])


# ### Acceder a ciertas columnas o filas

# In[16]:


(data.Name == data['Name']).all()


# ## Un pandas "Series" es lo que le decimos a una columna de un DataFrame. Se exponen varios métodos ahí mismo, que hace que sea muy fácil preguntar cosas de él.

# ### ¿Cuál es el "total" más grande?

# In[12]:


data['Total'].max()


# In[13]:


data['Attack'].max()


# ### ¿Quién tiene el total más grande?

# In[23]:


total_mas_grande = data['Total'].max()


# In[27]:


data[data['Total'] == total_mas_grande]['Name']


# ### ¿Cuál es la velocidad "Speed" promedio?

# In[29]:


data['Speed'].mean()


# ### ¿Cómo son los valores del estadístico "Attack"?

# In[32]:


get_ipython().magic('matplotlib inline')


# #### Pandas nos permite hacer muchas visualizaciones desde el Series o DataFrame mismo, haciéndolo muy fácil obtener una vista ancha de la forma de tus datos.

# In[33]:


data['Attack'].hist()


# ### Solo para estar seguro..

# In[34]:


data['Attack'].min()


# In[35]:


data['Attack'].max()


# ### Cuantos de cada "Type 1" y "Type 2" tenemos?

# # "Aggregation"

# ## ¿Cuál es el "Total" promedio de cada Pokémon de "Type 1" y "Type 2"?

# In[42]:


data.groupby('Type 2')['Total'].mean().sort_values(ascending=False)


# ## ¿Cuál es el "Attack" máximo de cada combinación de "Type 1" y "Type 2"?

# In[46]:


data.groupby(['Type 1', 'Type 2'])['Attack'].max().sort_values(ascending=False)


# # Visualizar con seaborn

# In[49]:


import seaborn as sns


# ## Visualizar una columna contra otra

# In[51]:


sns.jointplot(x='Sp. Atk', y='Sp. Def', data=data, kind='reg')


# In[50]:


data.head()


# ## Crear un boxplot de las columnas que nos importan

# In[53]:


sns.boxplot(data = data.drop(['Name', 'Total'], axis=1).head())

