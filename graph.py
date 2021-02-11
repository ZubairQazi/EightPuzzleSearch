import matplotlib.pyplot as plt

X = [0, 2, 4, 8, 12, 16, 20, 24]

Uniform_Nodes = [0, 7, 48, 474, 3377, 22778]
Misplaced_Nodes = [0, 2, 4, 18, 181, 1083, 5034, 30020]
Manhattan_Nodes = [0, 2, 4, 12, 43, 141, 765, 2609]

plt.subplot(2, 1, 1)

plt.plot(X[:6], Uniform_Nodes, label='Uniform Cost')
plt.plot(X, Misplaced_Nodes, label='Misplaced')
plt.plot(X, Manhattan_Nodes, label='Manhattan')

plt.xticks(X)
plt.title('Nodes Expanded vs. Solution Depth')
plt.legend()

plt.subplot(2, 1, 2)

Uniform_Size = [0, 10, 42, 299, 1985, 11633]
Misplaced_Size = [0, 4, 9, 30, 170, 818, 3665, 19072]
Manhattan_Size = [0, 4, 9, 22, 56, 131, 651, 2126]

plt.plot(X[:6], Uniform_Size, label='Uniform Cost')
plt.plot(X, Misplaced_Size, label='Misplaced')
plt.plot(X, Manhattan_Size, label='Manhattan')

plt.xticks(X)
plt.title('Max Queue Size vs. Solution Depth')
plt.legend()

plt.tight_layout()
plt.show()



