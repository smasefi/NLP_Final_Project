# Samantha Asefi (sma9am@virginia.edu)
# DS 5001
# 8 May 2026
 
import subprocess
import sys
from pathlib import Path
 

notebooks = [
    "01_fetchdata.ipynb",
    "02_cleandata.ipynb",
    "03_bow_tfidf.ipynb",
    "04_pca.ipynb",
    "05_lda.ipynb",
    "06_word2vec.ipynb",
    "07_sentiment_analysis.ipynb",
    "08_hierarchial.ipynb",
]
 
for nb in notebooks:
    print(f"\n{'='*50}")
    print(f"Running {nb}...")
    print('='*50)
 
    result = subprocess.run(
        [sys.executable, "-m", "nbconvert",
         "--to", "notebook",
         "--execute",
         "--inplace",
         "--ExecutePreprocessor.timeout=3600",
         nb],
        capture_output=True,
        text=True
    )
 
    if result.returncode != 0:
        print(f"ERROR in {nb}:")
        print(result.stderr)
        sys.exit(1)
    else:
        print(f"✓ {nb} completed successfully")
 
print("\n✓ All notebooks completed successfully")
 