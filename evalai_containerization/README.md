# EvalAI CLI Container (legacy)

> **⚠️ Legacy path.** The 2025 STORM-AI challenge was hosted on **Codabench**, not EvalAI. This container helper is kept for reference only; see the [submission tutorial](https://2025-ai-challenge.readthedocs.io/en/latest/submission.html) for the workflow that was actually used.

Here we provide a `Dockerfile` that you can use in case you are experiencing issues installing or using the `EvalAI CLI Tool`. To get started, install `docker` (you can follow the [installation guide](https://2025-ai-challenge.readthedocs.io/en/latest/installation.html) in the wiki). Then, edit the `Dockerfile` to add your **EvalAI token** where it is indicated.



## Building the Image  

Once you have edited the `Dockerfile`, build the image by navigating to the download folder, opening a terminal, and running the following command:

```bash
docker build -t evalai-cli:latest .
```



## Testing the Container  

After the image has been successfully built, you can test it to ensure everything works properly. Run the following command:

```bash
docker run evalai-cli:latest teams --participant
```

If the teams you have created on the EvalAI platform appear, the setup is correct.  
If you do not see this message, you have likely entered your EvalAI token incorrectly in the `Dockerfile`. Edit it, rebuild the image, and try again.


## Submitting Through the Container  

To submit your work using the container, run the following command:

```bash
docker run -it --rm --user root -v /var/run/docker.sock:/var/run/docker.sock evalai-cli:latest push storm-ai-submission:latest --phase mit-competition-2394
```

Here:
-  `storm-ai-submission:latest` is your submission image.
- `--phase mit-competition-2394` specifies the phase for your submission.

Now you should be able to upload any of you images to the challenge.