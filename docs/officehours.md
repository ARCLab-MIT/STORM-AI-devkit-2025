# Office Hours

## Transcripts
<!-- Search Bar -->
<!-- Q&A Section -->
<div class="faq-container" style="font-family: Arial, sans-serif;">
  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      February 12, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">No transcript available</p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      February 19, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">[Organizer 1] 17:04:42
      Okay, I think we can get started. If everyone has any questions, feel free to ask.
      [Participant 1] 17:05:31
      I have a question regarding the libraries. Are we allowed to use any of the libraries or there are the limitations that we have to use certain libraries for this project?
      [Participant 1] 17:05:43
      Because the libraries was not mentioned in the GitHub repository or anywhere from where the data sources was being downloaded.
      [Organizer 2] 17:05:57
      I… Yeah, I think that as long as you as you provide the libraries that you are using in the environment demo file is not going to be any kind of probably with that.
      [Organizer 1] 17:05:57
      Go on a second.
      [Organizer 2] 17:06:26
      But keep in mind that you have to that the libraries that you use have to be like Micro Konda, Micromambamba.
      [Participant 1] 17:06:26
      Thank you.
      [Organizer 2] 17:06:37
      Is able to install on their dependencies dependencies that do need to run your script so check that before submitting anything?
      [Organizer 2] 17:06:49
      With all that said, you won't have any kind of trouble.
      [Participant 1] 17:06:54
      Sure, sure.
      [Organizer 2] 17:06:58
      You're welcome.
      [Participant 1] 17:11:56
      This submission for this project is being postponed to 21st April, right?
      [Organizer 2] 17:12:03
      Yeah, yesterday, I think that yesterday it was yesterday when we announced that we are moving the deadline to The 21st, yeah.
      [Organizer 2] 17:12:20
      And also you should have 10 extra submissions so don't worry on going over in the submission process.
      [Organizer 2] 17:12:31
      Because we gave you a little bit more submission.
      [Organizer 1] 17:12:42
      Hello, Participant 3. So you just joined the call if you have any question we'll just feel free to ask any question. We're just waiting for new participant if they need any help.
      [Participant 2] 17:12:55
      I actually had one question. As I was like processing the density data, I think this was asked in the forum. I don't recall what the answer was. Maybe it was already resolved.
      [Participant 2] 17:13:05
      But some of the density data has like values of like like 9e to the 32. Is this like supposed to be treated as like noise or Or like the true, I mean, obviously it's not the true value because it seems to be like a non-trending value.
      [Participant 2] 17:13:26
      Are we supposed to handle these by like throwing these density data away or Yeah, how would we like handle those like particular rows?
      [Organizer 2] 17:13:36
      Yeah, exactly. Those are like Python, float 32 infinite values So yeah, you have to discard all of them.
      [Participant 2] 17:13:48
      Okay, sounds good.
      [Organizer 2] 17:13:51
      Also, it could be some values that are over CETO, like, I don't know.
      [Organizer 2] 17:14:00
      1 to a power of 20 or something like that, you also have to discard the those So we only have values, real values are just the only one that are under 10 to the minus 7.
      [Participant 2] 17:14:17
      I see. So we should, anything above 10 to the negative 7.
      [Participant 2] 17:14:22
      We should throw away essentially in the density data.
      [Organizer 2] 17:14:25
      Yeah, that's it.
      [Participant 3] 17:14:31
      I just got a couple questions here. About the submissions.
      [Participant 3] 17:14:38
      The first one, I'm guessing for the 80 submission limit is per team, not per a person.
      [Organizer 2] 17:14:47
      Yeah, it's per team.
      [Participant 3] 17:14:49
      Per team okay um Another question is, did you guys So we had a submission. Did you guys like rerun them? Because we had one and then it seemed like another one came through and we got a different score.
      [Participant 3] 17:14:59
      So I was wondering if you guys would be
      [Organizer 2] 17:15:03
      Yeah, we will run maybe you have one that has a perfect score Like one.
      [Participant 3] 17:15:08
      Yeah, yeah, yeah. That's what happened, yeah.
      [Organizer 2] 17:15:11
      Yeah, we have some errors in the scoring file. So we have to rerun it.
      [Participant 3] 17:15:16
      Okay, so you guys, so now… Okay, so you re-ran them and now that's the correct score now is what's in there.
      [Organizer 2] 17:15:25
      Yeah. That's correct.
      [Participant 3] 17:15:26
      Okay. And then let me just clarify with the ghost data. I think I saw in the discussion that you guys are going to go back through and add some of the missing files.
      [Organizer 3] 17:15:40
      Yeah, the way that that works is there are multiple satellites and we were just missing data from a couple of them that covered the time frame that's missing.
      [Organizer 3] 17:15:49
      And we were not aware of that. Until somebody pointed it out. So we're just going to go back through and we'll process that data from the satellites that we initially didn't have.
      [Participant 3] 17:16:00
      Okay. I need to just throw it in that Dropbox, same Dropbox.
      [Organizer 3] 17:16:03
      Yep. And we will send out an email whenever that goes up.
      [Participant 3] 17:16:07
      Okay. And then, yeah, I think that's… I think that's all I had. Thank you.
      [Organizer 2] 17:16:20
      In any case, we try to keep the wiki app like updated So if you are looking into the different versions of the wiki, you could see if we made any change So try to use the wiki as your guidance.
      [Participant 2] 17:25:14
      Hello. Yes, since someone's asking a question, if I could maybe ask maybe a little more obvious question, just like more of a confirmation It seems like the performance metrics or the scoring is based on the MSIS baseline I'm assuming that means that you guys are taking the initial state and then
      [Participant 2] 17:25:37
      Using the propagation. With the MSIS model at the locations of the propagator's states and then using that to compare against the true densities provided by the the spacecraft data sets that you provided.
      [Participant 2] 17:25:53
      Is that the case where that's what you're comparing? They're using the MSS to in line with the density inputs for the propagator
      [Organizer 2] 17:26:13
      Yeah, well, what we do is that we… Yes, introduce to the proprietor the MCIS model.
      [Organizer 2] 17:26:22
      We give to it the initial state and just retrieve the density values.
      [Organizer 2] 17:26:28
      And then we apply our rolling mean to get the orbital mean the orbital mean values.
      [Organizer 2] 17:26:37
      And to do so, to establish the window size we use the mean motion so we have we know more or less what is the orbital And… the orbit video.
      [Organizer 2] 17:26:56
      So that is how are we… scoring the MCs this slide.
      [Participant 2] 17:27:03
      Got it. And for the density predictions.
      [Participant 2] 17:27:10
      Well, obviously, I'm using… like the data set itself for like train test splitting But when the scoring is done, I'm assuming those like large values we mentioned, like the E, Any values above e to the negative 7.
      [Participant 2] 17:27:27
      When the predictions are being generated from the model. They're going to generate predictions for those indices and maybe on your evaluation, you'll have those metrics and then the errors will be compared to that metric.
      [Participant 2] 17:27:43
      Will you guys be throwing it away on your side as well for the prediction or for the estimation?
      [Participant 2] 17:27:47
      Or rather for the… For the scoring or should we like, what should we put in those indices where those predictions occur.
      [Participant 2] 17:27:58
      For comparison, should we put like zero or… put that in.
      [Organizer 2] 17:28:01
      Well you usually… Usually you are using machine learning models for other kinds of models.
      [Organizer 2] 17:28:09
      If you substitute those values with the number values with nons.
      [Organizer 2] 17:28:15
      It will work just fine. But what we do is to when we are going to score we apply as the threshold that you mentioned, 10 to the minus 7.
      [Organizer 2] 17:28:28
      On all the values that are over that scope, we are not taking into account in the scoring process.
      [Participant 2] 17:28:36
      Got it. Okay. Sounds good. So I'll kind of replicate that. I think like having… the scoring done on like a small like similar score to kind of evaluate how well the predictions are happening on my side before submitting would be helpful.
      [Participant 2] 17:28:55
      So I guess I will do the same approach. Yeah, thank you.
      [Organizer 2] 17:28:59
      Okay, great. Also, if you want the scoring script, you have it in the in the development kit of the challenge.
      [Participant 2] 17:29:09
      All right. Okay, I'll take a look at that too.
      [Organizer 2] 17:29:14
      Yeah, you can find it in the baseline directory as evaluation.py
      [Participant 2] 17:29:22
      Okay, sweet. Yeah, I haven't gotten that to that point yet, but I'll definitely check that out. That would save me a lot of time.
      [Participant 2] 17:29:28
      Thank you. Awesome. Take care.
      [Organizer 2] 17:29:29
      Sweet. You're welcome.
      </p>
  </details>
</div>
