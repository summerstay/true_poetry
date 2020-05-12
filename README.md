# true_poetry
Poetry generator by gpt-2 with meter and rhyme constraints. See a few examples at the bottom of this readme file.

required imports:

come with python: string, random, math, pickle

use pip or conda to install: torch, transformers 

Just run true_poetry.py and type or paste in some text as a prompt and it will generate a sonnet, limerick, couplets or a ballad. You should switch to 

model = GPT2LMHeadModel.from_pretrained("gpt2-xl") 

if you want it to automatically download the 6GB neural network. Gwern's finetumed poetry model does a somewhat better job, if you have a copy. It's a bit tricky to get working, though. In the same directory where true_poetry.py is, I have a folder called "poetry." In that folder sits Gwern's pytorch_model.bin and associated small files.

I downloaded all the files in a zipped tar file using this command:

rsync --verbose rsync://78.46.86.149:873/biggan/2019-12-13-gwern-gpt-2-1.5b-poetry-model-500522.tar.xz ./ 

this is the version for tensorflow. You then have to convert it for pytorch with the following command (adjust the path as needed):

%env OPENAI_GPT2_CHECKPOINT_PATH=/content/true_poetry/gwern

!transformers-cli convert --model_type gpt2 --tf_checkpoint model-500522
--config /content/true_poetry/gwern/config.json --pytorch_dump_output /

If that's too much work, just use the gpt2-xl file, it works fine.

As for fine-tuning your own model, Gwern's post about how he did it ( https://www.gwern.net/GPT-2 ) goes into enough detail that I was able to fine tune the 345M size model. But since gpt2-xl is so much better anyway, and it is impossible to train without special hardware, you are probably going to get better results by experimenting with finding just the right prompt and sticking with one of these two models than by training your own model.

You can modify the meter or rhyme scheme however you want.

There is still some work to be done. It likes short, one-token words too much. Sometimes the rhyming word is grammatically incorrect. The longer the poem goes, the more likely it is to degenerate.

If you have any good ideas on how to avoid passing a ton of variables or using a ton of globals in the recursive function grow_branches, I'd appreciate some help with programming style.

You can choose between limerick, ballad, or sonnet, or create your own rhyme scheme with a little editing of the code.

A few random samples. I have touched up just the punctuation by hand a bit:
__________________

BALLAD

And then with voice as sweet and small

as falling drops she said:

The night will come, it always comes,

with clouds, to change my bed

to snow. But in the night the moon

will put aside the stars,

and in the snow of clouds I will

be buried as you are.

__________________
SONNET

The mixture should continue beating when

you fold in half. The batter will be thick.

You can increase the speed by half and then

increase it further with the beat on stick.

The mixture will continue beating when

you fold in half and then begin to fold

in alternating thirds. You should begin

to notice little peaks, that seem to hold

the mixture from becoming soft. You will

be looking for to lift, or curt but still.

__________________
SONNET

I see myself in all, myself

in thee; I have been so from first

to last; I see the present self

of him I murdered in his burst

of song. I have undone myself,

and all, myself, in that; and my

revenge is now, or will be shelf'd.

I see the last. The last, and by

that I, the last. The last and best,

the last, and by which I am blessed.

__________________
OTHER

The snow began a little thick and white

and then a little loath; and then, the night,

The wind, and then again the snow; until

The sky above, a dark and endless, still

and empty sky: a sky, a sky. The night,

The moon and wind, the moon, and wind and, white.

__________________
OTHER

The children run, but cannot find

The house's ghosts; the ghost behind

The curtain calls, the ghost before

The curtains pull apart - The door,

The window open flies. But no--

The windows shut, and blinds below.

__________________
LIMERICK

The Maximus army were led

by Megatron Prime with his red,

mechanical arm,

at fist and forearm,

and he had his fire-flies red

__________________
LIMERICK

And then, as in dreams, she began

to move to her side: and the man

was dumbfounded. He

could sense each degree

of freedom in movement. I can

__________________
LIMERICK

And there was an Englishman who

had married his ex. and so grew

to hate and resent

his wife; And she went

to see that he lived. And the two

__________________
LIMERICK

There was a young lady aboard

a steamship. The sea? She ignored

the sea, she ignored

the sails, for on board

she saw, in the galley, my lord.
__________________
