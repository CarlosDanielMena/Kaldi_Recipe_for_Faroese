-------------------------------------------------------------------------------
                           Kaldi Recipe for Faroese
-------------------------------------------------------------------------------

Author                : Carlos Daniel Hernández Mena.

Programming Languages : Kaldi, Python3, Bash

Recommended use       : speech recognition.

-------------------------------------------------------------------------------
Description
-------------------------------------------------------------------------------

The "Kaldi Recipe for Faroese" is a code recipe intended to show how to use
the corpus "Ravnursson Faroese Speech and Transcripts" [1] to create automatic 
speech recognition systems using the Kaldi toolkit [2].

In order to set the scripts up, it is necessary to install minimum 
requirements and to specify some paths; all of these indicated in the 
"run.sh" script of the recipe.

-------------------------------------------------------------------------------
Running the recipe
-------------------------------------------------------------------------------

* Create a folder to run the recipe

 $ mkdir mkdir ~/recipe
 $ cd ~/recipe

* Download the Ravnursson Corpus

 $ curl --remote-name-all https://repository.clarin.is/repository/xmlui/bitstream/handle/20.500.12537/276{/RAVNURSSON.zip}
 
 $ unzip RAVNURSSON.zip
 
You will have to find a folder called RAVNURSSON with the following content:

 - RAVNURSSON
   - speech
   - LICENSE.txt
   - metadata.tsv
   - README.txt
   
Keep the path to that RAVNURSSON folder.
 
* Clone the recipe

 $ git clone https://github.com/CarlosDanielMena/Kaldi_Recipe_for_Faroese

 Inside the folder "Kaldi_Recipe_for_Faroese", you will find:
 
  - Kaldi_Recipe_for_Faroese
    - ravnursson
    - README.txt
    
Now you have to copy the folder ravnursson to the "egs" directory of your Kaldi installation

 $ cp Kaldi_Recipe_for_Faroese/ravnursson <path-to-your-kaldi-installation>/kaldi/egs
 
 $ cd <path-to-your-kaldi-installation>/kaldi/egs/ravnursson/s5
 
* Configuration of the recipe

It is supposed that you are in the folder:
<path-to-your-kaldi-installation>/kaldi/egs/ravnursson/s5

 - Open the file run.sh
 - Modify the line: 
 corpus_root=/<path-to-ravnursson-corpus>/RAVNURSSON
 
 You will have to update the varibale "corpus_root" with the path to the
 folder RAVNURSSON that you kept in a previous step.
 
 - If you don't have a GPU open the file cmd.sh
 and change the line:
 
 export cuda_cmd="run.pl --gpu 1"
 
 to
 
 export cuda_cmd="run.pl"
 
* Run the recipe

If your Kaldi installation works correctly you can just type:

 $ bash run.sh

-------------------------------------------------------------------------------
Citation
-------------------------------------------------------------------------------

When publishing results based on the models please refer to:

   Hernández Mena, Carlos Daniel. "Samrómur-Adolescents Kaldi Recipe 22.06". 
   Web Download. Reykjavik University: Language and Voice Lab, 2022.

Contact: Carlos Daniel Hernández Mena (carlos.mena@ciempiess.org)

License: CC BY 4.0

-------------------------------------------------------------------------------
Acknowledgements
-------------------------------------------------------------------------------

The author want to thank to Jón Guðnason, head of the Language and Voice Lab 
for providing computational power to make these models possible. We also want 
to thank to the "Language Technology Programme for Icelandic 2019-2023" which 
is managed and coordinated by Almannarómur, and it is funded by the Icelandic 
Ministry of Education, Science and Culture.

Special thanks to Annika Simonsen and to The Ravnur Project for making their 
"Basic Language Resource Kit"(BLARK 1.0) publicly available through the 
research paper "Creating a Basic Language Resource Kit for Faroese" 
https://aclanthology.org/2022.lrec-1.495.pdf

-------------------------------------------------------------------------------
References
-------------------------------------------------------------------------------

[1] Hernández Mena, Carlos Daniel; Simonsen, Annika. "Ravnursson Faroese 
    Speech and Transcripts". Web Downloading: 
    http://hdl.handle.net/20.500.12537/276

[2] Povey, D., Ghoshal, A., Boulianne, G., Burget, L., Glembek, O., Goel, 
    N., ... & Vesely, K. (2011). The Kaldi speech recognition toolkit. In 
    IEEE 2011 workshop on automatic speech recognition and understanding 
    (No. CONF). IEEE Signal Processing Society.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

