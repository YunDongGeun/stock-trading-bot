import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 생성
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 3))

# 첫 번째 서브플롯 설정
ax1.plot(np.random.rand(50), color='red')
ax1.set_title('Plot 1')

# 두 번째 서브플롯 설정
ax2.bar(np.arange(10), np.random.rand(10))
ax2.set_title('Plot 2')

# 레이아웃 조정
plt.tight_layout()

# 피겨 표시
plt.show()