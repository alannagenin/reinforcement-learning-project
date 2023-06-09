import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores, highscore):
    '''
    Plot the game results.

    Parameters
    ----------
    scores : list
        scores
    mean_scores : list
        mean scores
    '''
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()

    plt.title("Training snake AI")
    plt.xlabel('# games')
    plt.ylabel('Score')

    plt.plot(scores, label="Score", c="#6A3D9A", linewidth=2)
    plt.plot(mean_scores, label="Mean score", c="mediumvioletred", linewidth=2)
    plt.ylim(ymin=0)

    plt.legend(frameon=False)

    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(round(mean_scores[-1], ndigits=2)))
    plt.text(0, highscore*0.85, f'High score: {highscore}')
    plt.show(block=False)
    plt.pause(.1)
