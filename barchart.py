import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .1

korea_scores = (554, 536, 538)
canada_scores = (510, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)
k1 = plt.bar(index, korea_scores, bar_width, alpha=.4, label="Korea")
c1 = plt.bar(index + 0.1, canada_scores, bar_width, alpha=.4, label="Canada")
ch1 = plt.bar(index + 0.2, china_scores, bar_width, alpha=.4, label="China")
f1 = plt.bar(index + 0.3, france_scores, bar_width, alpha=.4, label="France")

plt.title("Test scores by country")
plt.ylabel("Mean score is PISA 2012")
plt.xlabel("These are a subject")
plt.xticks(index + .3 / 2, ("Mathematics", "Reading", "Science"))
plt.legend()
plt.grid(True)

plt.show()
