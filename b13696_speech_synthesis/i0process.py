from encoder.params_model import model_embedding_size as speaker_embedding_size
from utils.argutils import print_args
from utils.modelutils import check_model_paths
from synthesizer.inference import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
from pathlib import Path
import numpy as np
import soundfile as sf
import librosa
import argparse
import torch
import sys
import os
from audioread.exceptions import NoBackendError

if __name__ == '__main__':
    ## Info & args
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-e", "--enc_model_fpath", type=Path, 
                        default="encoder/saved_models/pretrained.pt",
                        help="Path to a saved encoder")
    parser.add_argument("-s", "--syn_model_fpath", type=Path, 
                        default="synthesizer/saved_models/pretrained/pretrained.pt",
                        help="Path to a saved synthesizer")
    parser.add_argument("-v", "--voc_model_fpath", type=Path, 
                        default="vocoder/saved_models/pretrained/pretrained.pt",
                        help="Path to a saved vocoder")
    parser.add_argument("--cpu", action="store_true", help=\
        "If True, processing is done on CPU, even when a GPU is available.")
    parser.add_argument("--no_sound", action="store_true", help=\
        "If True, audio won't be played.")
    parser.add_argument("--seed", type=int, default=None, help=\
        "Optional random number seed value to make toolbox deterministic.")
    parser.add_argument("--no_mp3_support", action="store_true", help=\
        "If True, disallows loading mp3 files to prevent audioread errors when ffmpeg is not installed.")
    args = parser.parse_args()
    print_args(args, parser)
    if not args.no_sound:
        import sounddevice as sd

    if args.cpu:
        # Hide GPUs from Pytorch to force CPU processing
        os.environ["CUDA_VISIBLE_DEVICES"] = ""

    if not args.no_mp3_support:
        try:
            librosa.load("samples/1320_00000.mp3")
        except NoBackendError:
            print("Librosa will be unable to open mp3 files if additional software is not installed.\n"
                  "Please install ffmpeg or add the '--no_mp3_support' option to proceed without support for mp3 files.")
            exit(-1)
        
    print("Running a test of your configuration...\n")
        
    if torch.cuda.is_available():
        device_id = torch.cuda.current_device()
        gpu_properties = torch.cuda.get_device_properties(device_id)
        ## Print some environment information (for debugging purposes)
        print("Found %d GPUs available. Using GPU %d (%s) of compute capability %d.%d with "
            "%.1fGb total memory.\n" % 
            (torch.cuda.device_count(),
            device_id,
            gpu_properties.name,
            gpu_properties.major,
            gpu_properties.minor,
            gpu_properties.total_memory / 1e9))
    else:
        print("Using CPU for inference.\n")
    
    ## Remind the user to download pretrained models if needed
    check_model_paths(encoder_path=args.enc_model_fpath,
                      synthesizer_path=args.syn_model_fpath,
                      vocoder_path=args.voc_model_fpath)
    
    ## Load the models one by one.
    print("Preparing the encoder, the synthesizer and the vocoder...")
    encoder.load_model(args.enc_model_fpath)
    synthesizer = Synthesizer(args.syn_model_fpath)
    vocoder.load_model(args.voc_model_fpath)
    
    
    ## Run a test
    print("Testing your configuration with small inputs.")
    # Forward an audio waveform of zeroes that lasts 1 second. Notice how we can get the encoder's
    # sampling rate, which may differ.
    # If you're unfamiliar with digital audio, know that it is encoded as an array of floats 
    # (or sometimes integers, but mostly floats in this projects) ranging from -1 to 1.
    # The sampling rate is the number of values (samples) recorded per second, it is set to
    # 16000 for the encoder. Creating an array of length <sampling_rate> will always correspond 
    # to an audio of 1 second.
    print("\tTesting the encoder...")
    encoder.embed_utterance(np.zeros(encoder.sampling_rate))
    
    # Create a dummy embedding. You would normally use the embedding that encoder.embed_utterance
    # returns, but here we're going to make one ourselves just for the sake of showing that it's
    # possible.
    embed = np.random.rand(speaker_embedding_size)
    # Embeddings are L2-normalized (this isn't important here, but if you want to make your own 
    # embeddings it will be).
    embed /= np.linalg.norm(embed)
    # The synthesizer can handle multiple inputs with batching. Let's create another embedding to 
    # illustrate that
    embeds = [embed, np.zeros(speaker_embedding_size)]
    texts = ["test 1", "test 2"]
    print("\tTesting the synthesizer... (loading the model will output a lot of text)")
    mels = synthesizer.synthesize_spectrograms(texts, embeds)
    
    # The vocoder synthesizes one waveform at a time, but it's more efficient for long ones. We 
    # can concatenate the mel spectrograms to a single one.
    mel = np.concatenate(mels, axis=1)
    # The vocoder can take a callback function to display the generation. More on that later. For 
    # now we'll simply hide it like this:
    no_action = lambda *args: None
    print("\tTesting the vocoder...")
    # For the sake of making this test short, we'll pass a short target length. The target length 
    # is the length of the wav segments that are processed in parallel. E.g. for audio sampled 
    # at 16000 Hertz, a target length of 8000 means that the target audio will be cut in chunks of
    # 0.5 seconds which will all be generated together. The parameters here are absurdly short, and 
    # that has a detrimental effect on the quality of the audio. The default parameters are 
    # recommended in general.
    vocoder.infer_waveform(mel, target=200, overlap=50, progress_callback=no_action)
    
    print("All test passed! You can now synthesize speech.\n\n")
    
    
    ## Interactive speech generation
    print("This is a GUI-less example of interface to SV2TTS. The purpose of this script is to "
          "show how you can interface this project easily with your own. See the source code for "
          "an explanation of what is happening.\n")
    
    print("Interactive generation loop")
    num_generated = 0
    '''
    mysentences = [
    "Swarm, together with Whisper, is essential for Ethereum and even the whole decentralized network.",
    " After we established the Swarm Association with like-minded people in Switzerland very early, ",
    "the funds were jointly supported by Bitcoin Suisse and Ethereum Foundation, and the team was reorganized many times. ",
    "However, we think that the development of Swarm has completely deviated, ",
    "and we don't want Swarm to be a way for others to collect funds. ",
    "Still, Ethereum has no right to restrain others' behaviors, ",
    "so Ethereum Foundation can only divest the Swarm project. ",
    "We originally intended to complete thermal storage with an open mind and wanted Swarm to become a leader in thermal storage.",
    " If Ethereum is compared to a core of CPU, IPFS is compared to a hard disk, ",
    "and Swarm is the memory, in this way, a perfect decentralized network will be born, ",
    "which is the world computer in my mind. Swarm is not from Ethereum, but for everyone."
    ]
    '''

    '''
    mysentences = [
    "ctually, I think that the efforts of Leet Squad, Bee team, Bee-JS, ",
    "and others have made Swarm achieve great success in the technical direction.",
    "However, during the idle period of Swarm, miners' rights and interests were damaged due to lack of stimulation. ",
    "Under the condition of keeping the original architecture unchanged, we believe that Swarm must be stripped from Ethereum Foundation",
    " and we will reshape the value of Swarm in the form of a Swarm plug-in ",
    "to make up for the ecological benefits of BZZ during the idle period, ",
    "and help Swarm maintain and improve the ecology. ",
    "We can call the Swarm added with a plug-in as Swarm+, ",
    "and Ethereum will work with Swarm team to jointly ",
    "improve the thermal storage section of a decentralized world. "
    ]
    '''
    

    # mysentences = [
    # "The decentralized world in my mind is free and equal, ",
    # "just like Ethereum, I hope it is a core in this decentralized network, ",
    # "and I also hope that more excellent cores will appear so that Gavin Wood can realize his cross-chain,",
    # " heter genius and composite decentralized platform, ",
    # "which is the direction of the decentralized world. ",
    # "Swarm only completes the efficient data storage and distribution services between Ethereum and IFPS. ",
    # "Ethereum is just to perfect her, for She is our common child. "

    #  ]


    
    mysentences = [
    "The plug-in added by Ethereum to Swarm is only to compensate the miners for the damages", 
    " caused by an idle period of Swarm, while e b z z will reshape the value of Swarm. ", 
    "e b z z does not belong to Ethereum, nor an organization or a team. ", 
    "We will clearly announce the e b z z model, and we will take care of our common child again and carefully. ",
    "I used to say that I respect BitTorrent very much, ",
    "for it is the first decentralized sharing platform in the Internet world, ",
    "and it can be deemed the blazer of the Ethereum blueprint. ",
    "In this case, I want to influence others with our actions,",
    " and e b z z is just the value carrier for the links between Swarm sharers. Thank you. "
    ]
    

    '''
    mysentences = [
    
    "Swarm, together with Whisper, is essential for Ethereum and even the whole decentralized network.",
    "After we established the Swarm Association with like-minded people in Switzerland very early",
    "This is a test record. It's friday night. Let's start recording"
    ]
    '''

        # Get the reference audio filepath
    message = "Reference voice: enter an audio filepath of a voice to be cloned (mp3, " \
              "wav, m4a, flac, ...):\n"
    in_fpath = Path("whole_orig.wav".replace("\'", ""))
    #in_fpath = Path("original.wav".replace("\'", ""))
    # in_fpath = Path(input(message).replace("\"", "").replace("\'", ""))
    print(in_fpath,'#'*20, in_fpath.suffix.lower() , args.no_mp3_support)
    if in_fpath.suffix.lower() == ".mp3" and args.no_mp3_support:
        print("Can't Use mp3 files please try again:")
        
    ## Computing the embedding
    # First, we load the wav using the function that the speaker encoder provides. This is 
    # important: there is preprocessing that must be applied.
    
    # The following two methods are equivalent:
    # - Directly load from the filepath:
    preprocessed_wav = encoder.preprocess_wav(in_fpath)
    # - If the wav is already loaded:
    original_wav, sampling_rate = librosa.load(str(in_fpath))
    preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
    print("Loaded file succesfully")
    
    # Then we derive the embedding. There are many functions and parameters that the 
    # speaker encoder interfaces. These are mostly for in-depth research. You will typically
    # only use this function (with its default parameters):
    embed = encoder.embed_utterance(preprocessed_wav)
    print("Created the embedding")

    # while True:
    for mysentence in mysentences:
        try:

            
            
            ## Generating the spectrogram
            # text = input("Write a sentence (+-20 words) to be synthesized:\n")
            text = mysentence
            print('tex=',text, '#'*10)
            # If seed is specified, reset torch seed and force synthesizer reload
            if args.seed is not None:
                torch.manual_seed(args.seed)
                synthesizer = Synthesizer(args.syn_model_fpath)

            # The synthesizer works in batch, so you need to put your data in a list or numpy array
            texts = [text]
            embeds = [embed]

            # abel
            # texts = ['Swarm, together with Whisper, is essential for Ethereum and even the whole decentralized network.',
            # 'After we established the Swarm Association with like-minded people in Switzerland very early'
            # ]
            # embeds = [embed.embed]
            
            # end of abel

            # If you know what the attention layer alignments are, you can retrieve them here by
            # passing return_alignments=True
            specs = synthesizer.synthesize_spectrograms(texts, embeds)
            print('#'*10, 'len(specs)=',len(specs))
            spec = specs[0]
            print("Created the mel spectrogram")
            
            
            ## Generating the waveform
            print("Synthesizing the waveform:")

            # If seed is specified, reset torch seed and reload vocoder
            if args.seed is not None:
                torch.manual_seed(args.seed)
                vocoder.load_model(args.voc_model_fpath)

            # Synthesizing the waveform is fairly straightforward. Remember that the longer the
            # spectrogram, the more time-efficient the vocoder.
            generated_wav = vocoder.infer_waveform(spec)
            
            
            ## Post-generation
            # There's a bug with sounddevice that makes the audio cut one second earlier, so we
            # pad it.
            generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")

            # Trim excess silences to compensate for gaps in spectrograms (issue #53)
            generated_wav = encoder.preprocess_wav(generated_wav)
            
            # Play the audio (non-blocking)
            if not args.no_sound:
                try:
                    sd.stop()
                    sd.play(generated_wav, synthesizer.sample_rate)
                except sd.PortAudioError as e:
                    print("\nCaught exception: %s" % repr(e))
                    print("Continuing without audio playback. Suppress this message with the \"--no_sound\" flag.\n")
                except:
                    raise
                
            # Save it on the disk
            filename = "output_folder/demo_output_%02d.wav" % num_generated
            print(generated_wav.dtype)
            sf.write(filename, generated_wav.astype(np.float32), synthesizer.sample_rate)
            num_generated += 1
            print("\nSaved output as %s\n\n" % filename)
            
            
        except Exception as e:
            print("Caught exception: %s" % repr(e))
            print("Restarting\n")
