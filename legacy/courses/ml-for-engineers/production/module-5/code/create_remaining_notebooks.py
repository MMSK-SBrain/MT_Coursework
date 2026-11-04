import json

# Base path
base = "/Volumes/Dev/Course_Generator/courses/ml-for-engineers/production/module-5/code/"

# Session 2: Patient Clustering Comparison
patient_nb = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Patient Clustering - Hierarchical & DBSCAN Comparison\n\n## Session 2: Comparing Clustering Algorithms on Healthcare Data\n\n**Objectives:** Compare K-Means, Hierarchical, and DBSCAN clustering on patient medical data"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import silhouette_score\nfrom scipy.cluster.hierarchy import dendrogram, linkage\nimport warnings\nwarnings.filterwarnings('ignore')\nprint('Ready!')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Generate Synthetic Patient Data"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["np.random.seed(42)\nn_patients = 800\n\n# Generate patient features\npatients = pd.DataFrame({\n    'age': np.random.randint(18, 85, n_patients),\n    'bmi': np.random.uniform(18, 40, n_patients),\n    'blood_pressure_sys': np.random.randint(90, 180, n_patients),\n    'blood_pressure_dia': np.random.randint(60, 120, n_patients),\n    'glucose': np.random.uniform(70, 200, n_patients),\n    'cholesterol': np.random.uniform(150, 300, n_patients),\n    'heart_rate': np.random.randint(60, 100, n_patients)\n})\n\nprint(f'Generated {len(patients)} patients')\npatients.head()"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Method 1: K-Means Clustering"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# Standardize\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(patients)\n\n# K-Means with k=4\nkmeans = KMeans(n_clusters=4, random_state=42)\npatients['cluster_kmeans'] = kmeans.fit_predict(X_scaled)\nsilhouette_kmeans = silhouette_score(X_scaled, patients['cluster_kmeans'])\nprint(f'K-Means Silhouette Score: {silhouette_kmeans:.4f}')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Method 2: Hierarchical Clustering"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# Create dendrogram\nlinkage_matrix = linkage(X_scaled[:200], method='ward')  # Subset for visualization\nplt.figure(figsize=(14, 6))\ndendrogram(linkage_matrix)\nplt.title('Hierarchical Clustering Dendrogram', fontsize=14, fontweight='bold')\nplt.xlabel('Patient Index')\nplt.ylabel('Distance')\nplt.tight_layout()\nplt.show()"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# Hierarchical clustering\nhierarchical = AgglomerativeClustering(n_clusters=4, linkage='ward')\npatients['cluster_hierarchical'] = hierarchical.fit_predict(X_scaled)\nsilhouette_hier = silhouette_score(X_scaled, patients['cluster_hierarchical'])\nprint(f'Hierarchical Silhouette Score: {silhouette_hier:.4f}')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Method 3: DBSCAN Clustering"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# DBSCAN\ndbscan = DBSCAN(eps=1.5, min_samples=10)\npatients['cluster_dbscan'] = dbscan.fit_predict(X_scaled)\nprint(f'DBSCAN found {len(set(patients[\"cluster_dbscan\"])) - (1 if -1 in patients[\"cluster_dbscan\"] else 0)} clusters')\nprint(f'Outliers: {(patients[\"cluster_dbscan\"] == -1).sum()} patients')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Comparison and Insights"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["print('\\nClustering Method Comparison:')\nprint('='*60)\nprint(f'K-Means: {len(set(patients[\"cluster_kmeans\"]))} clusters, Silhouette={silhouette_kmeans:.4f}')\nprint(f'Hierarchical: {len(set(patients[\"cluster_hierarchical\"]))} clusters, Silhouette={silhouette_hier:.4f}')\nprint(f'DBSCAN: {len(set(patients[\"cluster_dbscan\"])) - 1} clusters + outliers')\nprint('='*60)\nprint('\\nRecommendation: Use K-Means or Hierarchical for this dataset')\nprint('DBSCAN useful for outlier detection in patient data')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Summary\n\n**Key Learnings:**\n- K-Means: Fast, requires K\n- Hierarchical: Dendrogram useful, computationally expensive\n- DBSCAN: Finds outliers, no K needed\n- Choose based on data characteristics and business needs"]
        }
    ],
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(base + "patient-clustering-comparison.ipynb", "w") as f:
    json.dump(patient_nb, f, indent=1)

print("Created patient-clustering-comparison.ipynb")

# Session 3: News Clustering
news_nb = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# News Article Clustering with NLP\n\n## Session 3: Document Clustering and Topic Discovery\n\n**Objectives:** Apply clustering to text data, discover topics without labels"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.cluster import KMeans\nfrom sklearn.decomposition import TruncatedSVD\nfrom wordcloud import WordCloud\nimport warnings\nwarnings.filterwarnings('ignore')\nprint('Ready!')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Generate Synthetic News Articles"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["# Synthetic news articles\nsports_articles = [\n    'football soccer goal team player match win championship',\n    'basketball game score NBA finals team player championship',\n    'tennis match player tournament grand slam win',\n] * 100\n\ntech_articles = [\n    'artificial intelligence machine learning AI technology data',\n    'smartphone mobile app technology innovation software',\n    'cybersecurity hacking data breach security technology',\n] * 100\n\nbusiness_articles = [\n    'stock market investment trading finance economy',\n    'company earnings profit revenue business growth',\n    'startup venture capital funding investment business',\n] * 100\n\narticles = sports_articles + tech_articles + business_articles\ntrue_labels = ['Sports']*300 + ['Tech']*300 + ['Business']*300\n\ndf = pd.DataFrame({'text': articles, 'true_category': true_labels})\nprint(f'Total articles: {len(df)}')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## TF-IDF Vectorization"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["vectorizer = TfidfVectorizer(max_features=100, stop_words='english')\nX_tfidf = vectorizer.fit_transform(df['text'])\nprint(f'TF-IDF matrix shape: {X_tfidf.shape}')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## K-Means Clustering"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["kmeans = KMeans(n_clusters=3, random_state=42)\ndf['cluster'] = kmeans.fit_predict(X_tfidf)\nprint('\\nCluster distribution:')\nprint(df['cluster'].value_counts())"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Topic Discovery - Top Terms per Cluster"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["print('\\nTop terms per cluster:')\norder_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]\nterms = vectorizer.get_feature_names_out()\n\nfor i in range(3):\n    print(f'\\nCluster {i}:')\n    top_terms = [terms[ind] for ind in order_centroids[i, :10]]\n    print(', '.join(top_terms))"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Visualization with t-SNE"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["from sklearn.manifold import TSNE\n\ntsne = TSNE(n_components=2, random_state=42, perplexity=30)\nX_tsne = tsne.fit_transform(X_tfidf.toarray())\n\nplt.figure(figsize=(12, 8))\nfor i in range(3):\n    mask = df['cluster'] == i\n    plt.scatter(X_tsne[mask, 0], X_tsne[mask, 1], label=f'Cluster {i}', alpha=0.6, s=30)\nplt.title('News Articles Clustered (t-SNE Visualization)', fontsize=14, fontweight='bold')\nplt.legend()\nplt.tight_layout()\nplt.show()"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Summary\n\n**Key Learnings:**\n- TF-IDF converts text to numerical features\n- K-Means successfully groups similar articles\n- Topics emerge from top terms in each cluster\n- t-SNE helps visualize document clusters"]
        }
    ],
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(base + "news-clustering-unsupervised.ipynb", "w") as f:
    json.dump(news_nb, f, indent=1)

print("Created news-clustering-unsupervised.ipynb")

# Session 5: t-SNE
tsne_nb = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# t-SNE: Advanced Dimensionality Reduction\n\n## Session 5: t-SNE vs PCA for Visualization\n\n**Objectives:** Master t-SNE, compare to PCA, understand when to use each"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["import numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.datasets import load_digits\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.decomposition import PCA\nfrom sklearn.manifold import TSNE\nimport time\nimport warnings\nwarnings.filterwarnings('ignore')\nprint('Ready!')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Load MNIST Digits"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["digits = load_digits()\nX = digits.data\ny = digits.target\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\nprint(f'Data shape: {X.shape}')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Method 1: PCA (Fast, Linear)"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["start = time.time()\npca = PCA(n_components=2, random_state=42)\nX_pca = pca.fit_transform(X_scaled)\ntime_pca = time.time() - start\nprint(f'PCA time: {time_pca:.2f}s')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Method 2: t-SNE (Slow, Non-linear)"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["start = time.time()\ntsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)\nX_tsne = tsne.fit_transform(X_scaled)\ntime_tsne = time.time() - start\nprint(f't-SNE time: {time_tsne:.2f}s')\nprint(f't-SNE is {time_tsne/time_pca:.1f}x slower than PCA')"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Side-by-Side Comparison"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))\n\n# PCA\nfor digit in range(10):\n    mask = y == digit\n    ax1.scatter(X_pca[mask, 0], X_pca[mask, 1], label=str(digit), alpha=0.6, s=20)\nax1.set_title(f'PCA (Time: {time_pca:.2f}s)', fontsize=13, fontweight='bold')\nax1.legend(title='Digit', bbox_to_anchor=(1.05, 1), loc='upper left')\nax1.grid(True, alpha=0.3)\n\n# t-SNE\nfor digit in range(10):\n    mask = y == digit\n    ax2.scatter(X_tsne[mask, 0], X_tsne[mask, 1], label=str(digit), alpha=0.6, s=20)\nax2.set_title(f't-SNE (Time: {time_tsne:.2f}s)', fontsize=13, fontweight='bold')\nax2.legend(title='Digit', bbox_to_anchor=(1.05, 1), loc='upper left')\nax2.grid(True, alpha=0.3)\n\nplt.suptitle('PCA vs t-SNE: MNIST Digits Visualization', fontsize=15, fontweight='bold')\nplt.tight_layout()\nplt.show()"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Perplexity Comparison"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["fig, axes = plt.subplots(1, 3, figsize=(18, 5))\nperplexities = [5, 30, 50]\n\nfor idx, perp in enumerate(perplexities):\n    tsne_temp = TSNE(n_components=2, random_state=42, perplexity=perp, n_iter=500)\n    X_tsne_temp = tsne_temp.fit_transform(X_scaled[:500])  # Subset for speed\n    \n    scatter = axes[idx].scatter(X_tsne_temp[:, 0], X_tsne_temp[:, 1], \n                               c=y[:500], cmap='tab10', alpha=0.6, s=20)\n    axes[idx].set_title(f'Perplexity = {perp}', fontsize=12, fontweight='bold')\n    axes[idx].grid(True, alpha=0.3)\n\nplt.suptitle('Effect of Perplexity on t-SNE', fontsize=14, fontweight='bold')\nplt.tight_layout()\nplt.show()"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## When to Use PCA vs t-SNE?\n\n**Use PCA when:**\n- Speed is important\n- Need to transform new data\n- Want interpretable components\n- Global structure matters\n- Preprocessing for other algorithms\n\n**Use t-SNE when:**\n- Visualization is primary goal\n- Local structure matters\n- Have computational resources\n- Don't need to transform new data\n- Beautiful plots desired!\n\n**Recommendation:** Use PCA first, then t-SNE for final visualization!"]
        }
    ],
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(base + "tsne-advanced-visualization.ipynb", "w") as f:
    json.dump(tsne_nb, f, indent=1)

print("Created tsne-advanced-visualization.ipynb")
print("\nAll session notebooks created successfully!")

