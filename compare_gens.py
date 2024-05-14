import os
import imageio

# Get each gen# recovered_reward and stack them into a gif:

gens = [2,3,4,5]
images = []
for gen in gens:
    path = f'gen{gen}/recovered_reward.png'
    # Load the plt image: 
    images.append(imageio.imread(path))


imageio.mimsave('gens.gif', images, fps=1)

import matplotlib.pyplot as plt

# Put len(gens) suibfigs in a row:
fig, axs = plt.subplots(1, len(gens), figsize=(15, 5))
for i, gen in enumerate(gens):
    path = f'gen{gen}/recovered_reward.png'
    img = imageio.imread(path)
    axs[i].imshow(img)
    axs[i].set_title(f'Generation {gen}')
    axs[i].axis('off')
    # remove extra white space in between subplots:
    plt.subplots_adjust(wspace=-0.2)
plt.savefig('gens.png', bbox_inches='tight', dpi=300)