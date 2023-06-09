# :snake: Snake game

The aim of this project is to implement a snake game using Reinforcement Learning.
It will be a revisited game of Snake, where you have random items that can give you more points.

Two game modes are available:

- The human mode where the user can play with the arrows on the numeric keypad.
- The AI mode where an AI learns by itself to play the snake game

Three types of fruits exist in the game (only available for human snake):

- Apples worth 1 point (red fruit) :apple:
- Bananas worth 5 points (yellow fruit) :banana:
- Kiwis worth 10 points (green fruit) :kiwi_fruit:

## Quick start

```bash
git clone https://github.com/alannagenin/reinforcement-learning-project
cd reinforcement-learning-project
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Play snake game :video_game:

Here is the help menu to start playing!

```bash
 python3 main.py --help
# Usage: main.py [OPTIONS]

# Options:
#   --type [AI|HUMAN]  Type of game to compute.
#   --speed INTEGER    Snake speed
#   --help             Show this message and exit.
```

You can change the default values using the following commands:

```bash
 python3 main.py --type AI
 python3 main.py --type HUMAN
 python3 main.py --type HUMAN --speed 10
```

## Issues :warning:

If you encounter issues with `cuda` please refer yourself to this [issue](https://github.com/pytorch/pytorch/issues/30664).

```bash
raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
```

## Demonstration

Now lets play! :space_invader:

The snake grows as it eats the fruits. Here it is on the verge of eating an apple! :apple: 

![Snake](https://github.com/alannagenin/reinforcement-learning-project/blob/main/demo/snake.png)

This gif illustrates the snake game implemented with the AI. At first it hits a lot the walls or knocks himself out. As time goes, it gets better at it and gets bigger.

![Snake demo](https://github.com/alannagenin/reinforcement-learning-project/blob/main/demo/training.gif)

On the following graph we can see that the average score as we iterate over the number of games. There is a high variance in terms of winnings, but it is noticeable that the score improves as the game progresses compared to the first games.

![Snake training steps](https://github.com/alannagenin/reinforcement-learning-project/blob/main/demo/training_ai_snake.png)

## Contributors :woman_technologist: :man_technologist:

<a href="https://github.com/alannagenin/reinforcement-learning-project/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alannagenin/reinforcement-learning-project" />
</a>
