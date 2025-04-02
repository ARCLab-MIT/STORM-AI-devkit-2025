# Office Hours
Office hours are held weekly on Wednesdays from 11:00 am to 11:30 am EDT (UTC-04:00 → Please note time differences due to daylight savings!). Participants may ask general questions about the challenge (i.e. regarding data, submissions, evaluation, etc.), but all questions about specific approaches should be posted to the forums instead. Transcripts of the weekly office hours will be provided in the next section as they become available.
<div style="display: flex; justify-content: left; align-items: center; gap: 10px; padding: 10px;">
  <div style="display: inline-flex; align-items: center; background-color: #4d4d4d; color: #ffffff; border-radius: 5px; padding: 5px 10px; font-family: Arial, sans-serif; font-size: 14px; text-align: center;">
    <img src="https://github.com/user-attachments/assets/22255638-84ce-4f79-a4e9-7e51d517c428" alt="Codabench Logo" style="height: 20px; margin-right: 8px;">
    <a href="https://mit.zoom.us/j/92427066103" target="_blank" style="color: #ffffff; text-decoration: none;">
        Office Hours
      </a>
  </div>
</div>

## Transcripts
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
    <p style="margin-top: 10px; font-size: 14px; color: #555;">[Organizer 1] 17:04:42<br>
      Okay, I think we can get started. If everyone has any questions, feel free to ask.<br>
      [Participant 1] 17:05:31<br>
      I have a question regarding the libraries. Are we allowed to use any of the libraries or there are the limitations that we have to use certain libraries for this project?<br>
      [Participant 1] 17:05:43<br>
      Because the libraries was not mentioned in the GitHub repository or anywhere from where the data sources was being downloaded.<br>
      [Organizer 2] 17:05:57<br>
      I… Yeah, I think that as long as you as you provide the libraries that you are using in the environment demo file is not going to be any kind of probably with that.<br>
      [Organizer 1] 17:05:57<br>
      Go on a second.<br>
      [Organizer 2] 17:06:26<br>
      But keep in mind that you have to that the libraries that you use have to be like Micro Konda, Micromambamba.<br>
      [Participant 1] 17:06:26<br>
      Thank you.<br>
      [Organizer 2] 17:06:37<br>
      Is able to install on their dependencies dependencies that do need to run your script so check that before submitting anything?<br>
      [Organizer 2] 17:06:49<br>
      With all that said, you won't have any kind of trouble.<br>
      [Participant 1] 17:06:54<br>
      Sure, sure.<br>
      [Organizer 2] 17:06:58<br>
      You're welcome.<br>
      [Participant 1] 17:11:56<br>
      This submission for this project is being postponed to 21st April, right?<br>
      [Organizer 2] 17:12:03<br>
      Yeah, yesterday, I think that yesterday it was yesterday when we announced that we are moving the deadline to The 21st, yeah.<br>
      [Organizer 2] 17:12:20<br>
      And also you should have 10 extra submissions so don't worry on going over in the submission process.<br>
      [Organizer 2] 17:12:31<br>
      Because we gave you a little bit more submission.<br>
      [Organizer 1] 17:12:42<br>
      Hello, Participant 3. So you just joined the call if you have any question we'll just feel free to ask any question. We're just waiting for new participant if they need any help.<br>
      [Participant 2] 17:12:55<br>
      I actually had one question. As I was like processing the density data, I think this was asked in the forum. I don't recall what the answer was. Maybe it was already resolved.<br>
      [Participant 2] 17:13:05<br>
      But some of the density data has like values of like like 9e to the 32. Is this like supposed to be treated as like noise or Or like the true, I mean, obviously it's not the true value because it seems to be like a non-trending value.<br>
      [Participant 2] 17:13:26<br>
      Are we supposed to handle these by like throwing these density data away or Yeah, how would we like handle those like particular rows?<br>
      [Organizer 2] 17:13:36<br>
      Yeah, exactly. Those are like Python, float 32 infinite values So yeah, you have to discard all of them.<br>
      [Participant 2] 17:13:48<br>
      Okay, sounds good.<br>
      [Organizer 2] 17:13:51<br>
      Also, it could be some values that are over CETO, like, I don't know.<br>
      [Organizer 2] 17:14:00<br>
      1 to a power of 20 or something like that, you also have to discard the those So we only have values, real values are just the only one that are under 10 to the minus 7.<br>
      [Participant 2] 17:14:17<br>
      I see. So we should, anything above 10 to the negative 7.<br>
      [Participant 2] 17:14:22<br>
      We should throw away essentially in the density data.<br>
      [Organizer 2] 17:14:25<br>
      Yeah, that's it.<br>
      [Participant 3] 17:14:31<br>
      I just got a couple questions here. About the submissions.<br>
      [Participant 3] 17:14:38<br>
      The first one, I'm guessing for the 80 submission limit is per team, not per a person.<br>
      [Organizer 2] 17:14:47<br>
      Yeah, it's per team.<br>
      [Participant 3] 17:14:49<br>
      Per team okay um Another question is, did you guys So we had a submission. Did you guys like rerun them? Because we had one and then it seemed like another one came through and we got a different score.<br>
      [Participant 3] 17:14:59<br>
      So I was wondering if you guys would be<br>
      [Organizer 2] 17:15:03<br>
      Yeah, we will run maybe you have one that has a perfect score Like one.<br>
      [Participant 3] 17:15:08<br>
      Yeah, yeah, yeah. That's what happened, yeah.<br>
      [Organizer 2] 17:15:11<br>
      Yeah, we have some errors in the scoring file. So we have to rerun it.<br>
      [Participant 3] 17:15:16<br>
      Okay, so you guys, so now… Okay, so you re-ran them and now that's the correct score now is what's in there.<br>
      [Organizer 2] 17:15:25<br>
      Yeah. That's correct.<br>
      [Participant 3] 17:15:26<br>
      Okay. And then let me just clarify with the ghost data. I think I saw in the discussion that you guys are going to go back through and add some of the missing files.<br>
      [Organizer 3] 17:15:40<br>
      Yeah, the way that that works is there are multiple satellites and we were just missing data from a couple of them that covered the time frame that's missing.<br>
      [Organizer 3] 17:15:49<br>
      And we were not aware of that. Until somebody pointed it out. So we're just going to go back through and we'll process that data from the satellites that we initially didn't have.<br>
      [Participant 3] 17:16:00<br>
      Okay. I need to just throw it in that Dropbox, same Dropbox.<br>
      [Organizer 3] 17:16:03<br>
      Yep. And we will send out an email whenever that goes up.<br>
      [Participant 3] 17:16:07<br>
      Okay. And then, yeah, I think that's… I think that's all I had. Thank you.<br>
      [Organizer 2] 17:16:20<br>
      In any case, we try to keep the wiki app like updated So if you are looking into the different versions of the wiki, you could see if we made any change So try to use the wiki as your guidance.<br>
      [Participant 2] 17:25:14<br>
      Hello. Yes, since someone's asking a question, if I could maybe ask maybe a little more obvious question, just like more of a confirmation It seems like the performance metrics or the scoring is based on the MSIS baseline I'm assuming that means that you guys are taking the initial state and then<br>
      [Participant 2] 17:25:37<br>
      Using the propagation. With the MSIS model at the locations of the propagator's states and then using that to compare against the true densities provided by the the spacecraft data sets that you provided.<br>
      [Participant 2] 17:25:53<br>
      Is that the case where that's what you're comparing? They're using the MSS to in line with the density inputs for the propagator<br>
      [Organizer 2] 17:26:13<br>
      Yeah, well, what we do is that we… Yes, introduce to the proprietor the MCIS model.<br>
      [Organizer 2] 17:26:22<br>
      We give to it the initial state and just retrieve the density values.<br>
      [Organizer 2] 17:26:28<br>
      And then we apply our rolling mean to get the orbital mean the orbital mean values.<br>
      [Organizer 2] 17:26:37<br>
      And to do so, to establish the window size we use the mean motion so we have we know more or less what is the orbital And… the orbit video.<br>
      [Organizer 2] 17:26:56<br>
      So that is how are we… scoring the MCs this slide.<br>
      [Participant 2] 17:27:03<br>
      Got it. And for the density predictions.<br>
      [Participant 2] 17:27:10<br>
      Well, obviously, I'm using… like the data set itself for like train test splitting But when the scoring is done, I'm assuming those like large values we mentioned, like the E, Any values above e to the negative 7.<br>
      [Participant 2] 17:27:27<br>
      When the predictions are being generated from the model. They're going to generate predictions for those indices and maybe on your evaluation, you'll have those metrics and then the errors will be compared to that metric.<br>
      [Participant 2] 17:27:43<br>
      Will you guys be throwing it away on your side as well for the prediction or for the estimation?<br>
      [Participant 2] 17:27:47<br>
      Or rather for the… For the scoring or should we like, what should we put in those indices where those predictions occur.<br>
      [Participant 2] 17:27:58<br>
      For comparison, should we put like zero or… put that in.<br>
      [Organizer 2] 17:28:01<br>
      Well you usually… Usually you are using machine learning models for other kinds of models.<br>
      [Organizer 2] 17:28:09<br>
      If you substitute those values with the number values with nons.<br>
      [Organizer 2] 17:28:15<br>
      It will work just fine. But what we do is to when we are going to score we apply as the threshold that you mentioned, 10 to the minus 7.<br>
      [Organizer 2] 17:28:28<br>
      On all the values that are over that scope, we are not taking into account in the scoring process.<br>
      [Participant 2] 17:28:36<br>
      Got it. Okay. Sounds good. So I'll kind of replicate that. I think like having… the scoring done on like a small like similar score to kind of evaluate how well the predictions are happening on my side before submitting would be helpful.<br>
      [Participant 2] 17:28:55<br>
      So I guess I will do the same approach. Yeah, thank you.<br>
      [Organizer 2] 17:28:59<br>
      Okay, great. Also, if you want the scoring script, you have it in the in the development kit of the challenge.<br>
      [Participant 2] 17:29:09<br>
      All right. Okay, I'll take a look at that too.<br>
      [Organizer 2] 17:29:14<br>
      Yeah, you can find it in the baseline directory as evaluation.py<br>
      [Participant 2] 17:29:22<br>
      Okay, sweet. Yeah, I haven't gotten that to that point yet, but I'll definitely check that out. That would save me a lot of time.<br>
      [Participant 2] 17:29:28<br>
      Thank you. Awesome. Take care.<br>
      [Organizer 2] 17:29:29<br>
      Sweet. You're welcome.<br>
      </p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      February 26, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">No discussions to report.</p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      March 5, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">No discussions to report.</p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      March 12, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">A full transcript is unavailable. Participant questions revolved around Codabench submission logistics, and the organizers provided the following clarifications: (1) Participants may delete failed submissions to reduce their total number of submissions if they reach the limit. (2) Participants may not delete finished/scored runs to reduce their total number of submissions.</p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      March 19, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">No discussions to report.</p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      March 26, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">A full transcript is unavailable. The following announcements were distributed via our <a href="https://docs.google.com/forms/d/e/1FAIpQLSeatJPuSz5TY_nR7A-nCKTZqWwvHzIvnoN7Y3uOE1FtnbzXsQ/viewform?usp=sf_link">mailing list</a> and <a href="https://aeroastro.mit.edu/arclab/aichallenge/">landing page</a> in response to the attendees' questions:<br>
    <ol>
      <li><b>Complete Feedback Form:</b> We've noticed that while we have a large and engaged group of participants, only a limited number of teams have submitted their models so far. We understand that there can be many reasons for this, and we want to ensure that everyone has a positive and rewarding experience. To help us better understand your experience, please complete <a href="https://forms.gle/pypur1cHx2eqDgFA6">this short feedback form</a>.</li>
      <li><b>Submit Your Models:</b> From now on, please submit your model to the public leaderboard for both Phase 1.1 and 1.2! The challenge is coming to a close, and we're eager to see the innovative solutions you've developed. Moreover, sharing your results is an essential and valuable part of the Challenge since you can learn from the leaderboard and receive feedback.</li>
      <li><b>Final Score Computation:</b> As you know, recently we introduced a new task in Phase 1.2 to further challenge your models. To clarify the weighting scheme, this new dataset will account for 80% of the final score, while the original dataset will contribute 20%.</li>
      <li><b>Altitude Corrections:</b> We’ve corrected the altitude values in the Phase 1.2 dataset, they were mistakenly provided in kilometers, unlike Phase 1.1 where they were in meters. Now, all values are consistently in meters. Please ignore the column name "Altitude (km)", the values are in meters despite the label. We’ve kept the name unchanged to avoid breaking existing submissions.</li>
    </ol>
    </p>
  </details>

  <details style="margin-bottom: 10px; border: 1px solid #e0e0e0; border-radius: 5px; padding: 10px;">
    <summary style="font-size: 16px; font-weight: bold; cursor: pointer; color: #2b2b2b;">
      April 2, 2025
    </summary>
    <p style="margin-top: 10px; font-size: 14px; color: #555;">[Participant 1] 11:05:01<br>
    One, I think this may already be somewhat answered, but I noticed that on the wiki.<br>
    <br>
    [Participant 1] 11:05:11<br>
    The submission It's probably due to the fact that the wiki might be outdated.<br>
    <br>
    [Participant 1] 11:05:17<br>
    But the wiki states that you have to create a Speaking of two sides.<br>
    <br>
    [Participant 1] 11:05:31<br>
    I believe it was updated. But I noticed that somewhere it said it stated that you have to submit a predictions.json But in a different spot, it's mentioned to do a submission.json.<br>
    <br>
    [Participant 1] 11:05:46<br>
    I'm just trying to find where exactly that was.<br>
    <br>
    [Participant 1] 11:05:52<br>
    But we have to submit, the software has to develop or create a prediction.json at the end. Is that correct?<br>
    <br>
    [Organizer 1] 11:06:01<br>
    Well, did you already submit? I think yes.<br>
    <br>
    [Participant 1] 11:06:04<br>
    Yes. Yeah, I just wanted to, I guess, bring to attention that I can't find it anymore.<br>
    <br>
    [Organizer 1] 11:06:07<br>
    Yeah.<br>
    <br>
    [Participant 1] 11:06:13<br>
    That somewhere it stated in the documentation to generate a submission dot JSON. And I just wanted to bring that to your attention to update it For others.<br>
    <br>
    [Organizer 1] 11:06:22<br>
    Okay, you can send me an email with where it's located this mistake, then we can take care of it.<br>
    <br>
    [Participant 1] 11:06:27<br>
    Okay, no worries.<br>
    <br>
    [Organizer 1] 11:06:29<br>
    If you find it now, I mean, that's good too. Please send me an email in any case.<br>
    <br>
    [Participant 1] 11:06:33<br>
    Okay, no, I think it was maybe I'll look at the Git log or the… the commits, but perhaps he has updated since the last time I have jotted it down.<br>
    <br>
    [Participant 1] 11:06:44<br>
    The other thing I'm noticing is that In my last submission.<br>
    <br>
    [Participant 1] 11:06:50<br>
    Well, I guess what happens is like my submission is receiving nas um in both of the results.<br>
    <br>
    [Participant 1] 11:06:59<br>
    And I think it's because it's the, well, before it was my simulation was uh timing out Like I was going over the 4,200 seconds.<br>
    <br>
    [Participant 1] 11:07:10<br>
    I'm sorry, the 7200 seconds max time. But my latest submission was able to generate a prediction.json.<br>
    <br>
    [Participant 1] 11:07:21<br>
    For both of the tasks. And I can see in the um i can see in the log that it says submission successfully executed.<br>
    <br>
    [Participant 1] 11:07:30<br>
    And then at the end of the sim. Well, when I see these scoring logs For one of the tasks, it actually gives a score But for the other one, it says… I get this error, orbit mean density key not um<br>
    <br>
    [Participant 1] 11:07:50<br>
    Like not found, which is strange to me because… It's the same code that's generating the results.<br>
    <br>
    [Participant 1] 11:08:00<br>
    So that means that the prediction.json has this should have this key in both.<br>
    <br>
    [Participant 1] 11:08:06<br>
    But for one of the sim tasks it's uh it's failing to find this key, which usually means that it's just not finding the It's not loading in the JSON.<br>
    <br>
    [Participant 1] 11:08:18<br>
    Or maybe it is and it's just empty. I was wondering…<br>
    <br>
    [Organizer 1] 11:08:22<br>
    So you submitted the code could be evaluated for the two data sets we currently have.<br>
    <br>
    [Organizer 1] 11:08:29<br>
    In one case, you'll receive a result. With a score.<br>
    <br>
    [Participant 1] 11:08:32<br>
    Yes. Yep.<br>
    <br>
    [Organizer 1] 11:08:35<br>
    And this is for phase 1.1. 1.2.<br>
    <br>
    [Participant 1] 11:08:40<br>
    It received a score, I think, for phase 1.2. But not for 1.1<br>
    <br>
    [Organizer 1] 11:08:45<br>
    You'll receive it for 1.2, but not for 1.1. And in the case of 1.1 it tells you that in the JSON file there is a key that is missing.<br>
    <br>
    [Participant 1] 11:08:57<br>
    Yes.<br>
    <br>
    [Organizer 1] 11:08:59<br>
    Okay. I don't have an answer for this one. Unfortunately, so… I will pass this question to Sergio.<br>
    <br>
    [Organizer 1] 11:09:09<br>
    To double check since usually is the one that is checking more like the submission thing Were you able in the past to like did it happen already?<br>
    <br>
    [Participant 1] 11:09:13<br>
    Don't worry.<br>
    <br>
    [Organizer 1] 11:09:20<br>
    Like did you have a submitted for phase 1.1?<br>
    <br>
    [Participant 1] 11:09:24<br>
    So when you submit When you go to the submission page, it says selected tasks.<br>
    <br>
    [Participant 1] 11:09:32<br>
    And it's auto selected for both So I see that it should run for both tasks.<br>
    <br>
    [Organizer 1] 11:09:39<br>
    Yeah, you know, it should be in the sense in the past before we that we release the data set 1.2, let's say kind of like after the death is in 1.1. So I was wondering if you were able to<br>
    <br>
    [Participant 1] 11:09:43<br>
    Yeah.<br>
    <br>
    [Organizer 1] 11:09:52<br>
    Before running the code, but I suppose you already told me that before these you had some issues with the CPU time, right? So maybe the answer.<br>
    <br>
    [Participant 1] 11:09:58<br>
    Yeah, so I fixed that. I think so. And it's able to like it's able i see that the it says like it's generating the json file And that the submission like finished.<br>
    <br>
    [Organizer 1] 11:10:01<br>
    Okay.<br>
    <br>
    [Participant 1] 11:10:13<br>
    So, yeah.<br>
    <br>
    [Organizer 1] 11:10:14<br>
    I will pass this question to Sergio so we can double check Instead.<br>
    <br>
    [Organizer 1] 11:10:20<br>
    Okay, I mean, I'm also opening Codabench<br>
    <br>
    [Participant 1] 11:10:26<br>
    I think it's happening for other people too, but in the reverse situation I don't know if it's because like people said, I don't know, people submitted like as early as two days ago Or as late as two days ago. So that means that…<br>
    <br>
    [Participant 1] 11:10:41<br>
    It's almost as if the second scenario is happening where they're getting a score for the first one, but not the second one.<br>
    <br>
    [Participant 1] 11:10:51<br>
    So yeah.<br>
    <br>
    [Organizer 1] 11:10:51<br>
    Yeah, yeah, thank you. Thank you for letting me know. Yeah, also with the leaderboard, we're also trying to I think there is also a bug that the first one in the leaderboard, it has always NA instead of a number so we're trying to<br>
    <br>
    [Organizer 1] 11:11:05<br>
    We're already working on it in order to kind of like having maybe a different one page or a spreadsheet that takes the file from here and we can just you know put them in a new table in such a way we can also compute the total score because unfortunately again<br>
    <br>
    [Organizer 1] 11:11:19<br>
    Codabench does not allow, I think, to combine the score 1.1 with 1.2. So we have some comments about people that you know they didn't like this, let's say. So we're also working on that one on top of the, let's say modern issues okay<br>
    <br>
    [Organizer 1] 11:11:34<br>
    So yeah, please send me the email about the bug that one in the documentation.<br>
    <br>
    [Participant 1] 11:11:42<br>
    Okay. Yeah, I'll try to find it again. I thought I was able, should have been able to pull it up, but I guess I can't.<br>
    <br>
    [Participant 1] 11:11:49<br>
    But I'll let you know.<br>
    <br>
    [Organizer 1] 11:11:49<br>
    I mean, we edited a little bit recently at least we changed a few things so maybe maybe they solved it. But if you find it again, obviously, feel free to send it.<br>
    <br>
    [Participant 1] 11:11:58<br>
    Yeah.<br>
    <br>
    [Participant 1] 11:12:02<br>
    No. Yeah, no worries. Yeah.<br>
    <br>
    [Organizer 1] 11:12:02<br>
    You can also just send me an email. I didn't find it so it might be okay. So just… That would be appreciated. Thank you.<br>
    <br>
    [Participant 1] 11:12:09<br>
    Yeah, of course. Yeah, it looks like actually Yeah, I'll take a look. I'll take a look. And I'll try to like, anytime I find something like that, I'll… I'll go ahead and let you know.<br>
    <br>
    [Organizer 1] 11:12:22<br>
    Also, the discussion forum is fine wherever you want. You can do the discussion forum you can send me an email.<br>
    <br>
    [Participant 1] 11:12:24<br>
    And then… Oh, sure, sure.<br>
    <br>
    [Organizer 1] 11:12:28<br>
    You know, anywhere is fine.<br>
    <br>
    [Participant 1] 11:12:30<br>
    Yeah, I guess there was one thing that came up, but I already emailed you guys about it and it's already on the forums, which is uh If you use ORCID, Or rather, if you use PY MSIS in your model or like in your process procedure<br>
    <br>
    [Participant 1] 11:12:49<br>
    You can't actually get the latest space weather, so it will crash. So you have to like have a local copy of the space weather For MSIS.<br>
    <br>
    [Participant 1] 11:12:59<br>
    Reference that because the celestrack Even at my job, when I used celestrack to get the latest space weather, if you request it like many, many times they they blacklist your IP and you have to email Dr. Kelso directly and say, hey, my IP<br>
    <br>
    [Organizer 1] 11:13:19<br>
    Got it.<br>
    <br>
    [Participant 1] 11:13:19<br>
    It's blocked. So yeah, but that was already kind of… It's solved, I would say.<br>
    <br>
    [Organizer 1] 11:13:27<br>
    Was it an email sent to sector directly or to<br>
    <br>
    [Participant 1] 11:13:30<br>
    No, I sent it to the AI challenge email But yeah, you can take a look at that. I referenced like how I solved it. And then also there's like a forum page or forum post that addressed it as well, which helped<br>
    <br>
    [Organizer 1] 11:13:48<br>
    Perfect. Yeah. I was going to ask exactly that or if we from our side or from your side already posted also on the forum the workaround for that issue, let's say.<br>
    <br>
    [Organizer 1] 11:14:00<br>
    Okay, I'll go.<br>
    <br>
    [Participant 1] 11:14:00<br>
    Yeah. The other thing I've noticed is like the processor, the process time on Codabench is much slower than like let's say on my own pc uh So I had to kind of address that as well. I know that<br>
    <br>
    [Participant 1] 11:14:19<br>
    You mentioned, it was in a commit you made Let me try to find it here.<br>
    <br>
    [Participant 1] 11:14:32<br>
    Or propagator.<br>
    <br>
    [Organizer 1] 11:14:36<br>
    In the form the two, three seconds, three to five seconds you<br>
    <br>
    [Participant 1] 11:14:40<br>
    You made a git pay submit a git commit. And then you mentioned like CPU improvements or computational time improvements Like, for example, changing the test roll order. So it's like essentially you're doing J2 Changing the max step, changing the position tolerance, and removing effects to like SRP, solid tides<br>
    <br>
    [Participant 1] 11:15:04<br>
    And third body effects like sun and moon. It's interesting that, so these effects I already kind of did and in ORCID at least And you're saying that your CPU time is 2.5 to 3.5 seconds per sample.<br>
    <br>
    [Organizer 1] 11:15:08<br>
    Yep.<br>
    <br>
    [Participant 1] 11:15:20<br>
    What do you mean by per sample? Do you mean like per file ID for the<br>
    <br>
    [Organizer 1] 11:15:25<br>
    Per initial state. Like even…<br>
    <br>
    [Participant 1] 11:15:28<br>
    Yeah. So you're saying like it takes… like two to three seconds per iteration<br>
    <br>
    [Organizer 1] 11:15:39<br>
    So given the if the propagation is over three days, right? Is that what?<br>
    <br>
    [Participant 1] 11:15:42<br>
    Yeah, yeah. So you're saying it takes three seconds for a three-day propagation<br>
    <br>
    [Organizer 1] 11:15:44<br>
    That is one sample.<br>
    <br>
    [Organizer 1] 11:15:51<br>
    Yeah, I believe so. I think that one.<br>
    <br>
    [Participant 1] 11:15:53<br>
    Oh, okay. Yeah, I was not able to get that even with these conditions with ORCID.<br>
    <br>
    [Participant 1] 11:15:59<br>
    For some reason, and that's why it took a lot, like, that's why my sims were taking too long That's interesting because I guess I might have to like look back into how ORCID is doing Orchid is fun to use, but not so fun because the documentation is all in Java and<br>
    <br>
    [Participant 1] 11:16:18<br>
    We have to write it in Python.<br>
    <br>
    [Organizer 1] 11:16:19<br>
    I do agree with you. Can I ask you it might be… So I suppose, in essence, what I was going to say is that in my case I'm pretty sure I ran it also in the… Okay, so those CPU time now i don't perfectly remember if I tested them on<br>
    <br>
    [Organizer 1] 11:16:37<br>
    For example, we have a SuperCloud here, but I didn't use any parallel 19. So I might have tested locally, let's say, and I'm pretty sure I also tested them on Coda bench but I think they retrieve more or less the similar. So if it was not, for example, if I measure around four seconds locally, maybe in Codabench it was 4.5 seconds, okay? Maybe something like that.<br>
    <br>
    [Organizer 1] 11:16:58<br>
    So between these two locally and on CodaBench, I didn't see much discrepancy And another thing store, actually, let's answer this question. Do you notice these things? So when you run it locally, it takes, I don't know, a few seconds, but you're running on Coda bench, it takes much longer.<br>
    <br>
    [Participant 1] 11:17:15<br>
    It doesn't take much longer on CodaBench, that's for sure. But locally as well So I guess the thing is I am trying to do multiprocessing And I've still yet to kind of figure out maybe I'm doing my guess is that I'm not doing<br>
    <br>
    [Participant 1] 11:17:34<br>
    The initializations of stuff properly, like I'm doing more redundant things that I need to For example, like… Because ORCID is like using like this virtual environment or like virtual VM, essentially the virtual machine.<br>
    <br>
    [Participant 1] 11:17:49<br>
    For the Java instance. I kind of like naively initialized the virtual machine almost every process in the beginning.<br>
    <br>
    [Participant 1] 11:18:03<br>
    But I think you need to kind of abstract all those away so that you're able to multiprocess it properly.<br>
    <br>
    [Participant 1] 11:18:10<br>
    And have like independent propagations happening. Because once you start moving it to like multiple cores It still might have to reference the same kind of ORCID virtual machine.<br>
    <br>
    [Participant 1] 11:18:22<br>
    Or you make a virtual machine for each process.<br>
    <br>
    [Participant 1] 11:18:27<br>
    And then you keep that virtual machine and you replace it with a new propagation.<br>
    <br>
    [Participant 1] 11:18:33<br>
    So I kind of like i kind of dropped that for now and I just wrote my own J2, which is much faster.<br>
    <br>
    [Organizer 1] 11:18:40<br>
    I mean, yeah, sounds good too. So I got it. I never tried to run or a kid with parallel processing and so on.<br>
    <br>
    [Participant 1] 11:18:43<br>
    Yeah.<br>
    <br>
    [Organizer 1] 11:18:50<br>
    I might have heard from colleagues, past colleagues that maybe it's not possible. Maybe there is a way, but like you say, you need to, I don't know.<br>
    <br>
    [Organizer 1] 11:18:58<br>
    You need to do some trick or maybe run in a certain way so i'm also sure what you can and what you cannot parallelize in orchid Another thing that might take some time is because in my code.<br>
    <br>
    [Organizer 1] 11:19:10<br>
    Just because I don't know, let's say the participant, how direct the density in the code I'm just using obviously the anything like JP 2008 or any model of the density model that is already on orchid. So another thing that maybe you might check out is<br>
    <br>
    [Organizer 1] 11:19:26<br>
    How do you pass the density i believe you're using the, I mean, now you're using a different propagator okay but if you're using like the OriKit one you have the custom atmosphere model Is it correct? The one that we provided where inside you should give a function that given like the i suppose<br>
    <br>
    [Organizer 1] 11:19:42<br>
    Let's say position in time you can return the density such that the proper data can use it.<br>
    <br>
    [Organizer 1] 11:19:47<br>
    So maybe that part can also be something that since it's the part that you can as a participant change It might take a little bit longer i suppose I don't know. That's also suggesting. Maybe you already look at it maybe<br>
    <br>
    [Organizer 1] 11:20:01<br>
    It's not it's not going to solve anything.<br>
    <br>
    [Participant 1] 11:20:19<br>
    Yeah, for the first part, actually, I was just using the MSIS um atmospheric model. And I was just inputting custom APs and 10.7.7 values.<br>
    <br>
    [Participant 1] 11:20:36<br>
    So, yeah, I wasn't doing anything necessarily out of the original example there.<br>
    <br>
    [Participant 1] 11:20:42<br>
    But yeah, I think what I'm trying to aim for is use Orchid for the training.<br>
    <br>
    [Participant 1] 11:20:48<br>
    In terms of generating training data. And then when I do the submission, use a custom J2 code in Python, which is much faster at just doing what I need to. And I think that's good enough for the prediction as well.<br>
    <br>
    [Participant 1] 11:21:04<br>
    Yeah. Right, yes, yes, yes. J2 with the drag effects is mainly kind of what I've just stuck with for now and just writing that off.<br>
    <br>
    [Organizer 1] 11:21:06<br>
    Those include the drag, right?<br>
    <br>
    [Organizer 1] 11:21:14<br>
    Yeah, yeah, it's fine. I mean, I think it should be fine. When I say to, as you know, I mean, I guess if you're working also in this field or since you mentioned seller strike, the only thing that I did already So I know a few things. So OriKit is definitely not the most user friendly<br>
    <br>
    [Organizer 1] 11:21:27<br>
    Definitely is not, at least in my opinion but it's kind of like powerful but if you start to use it and follow the rules, right? Inside OriKit. So that's kind of like the the price to pay. And the other thing I did to make it a little bit faster yeah was basically to reduce the<br>
    <br>
    [Participant 1] 11:21:39<br>
    Yeah, yeah.<br>
    <br>
    [Organizer 1] 11:21:43<br>
    Instead of having J21 21 so for the setter sector and intestinal harmonics i just chose less let's say and that's mainly what does affect so actually even if you include the i think i tested again in the let's say after that post, even if you include those<br>
    <br>
    [Organizer 1] 11:22:03<br>
    Third body perturbation the solid tides that are totally minor perturbation in our case it doesn't really affect, at least in my script, it didn't really affect the computational time. And another thing that also improved was that change in the step. So putting the max step, I think, to 10,000 or something like that. So that one, because again we're using the propagator, sorry, we're using an integrator that is variable step so you decide what to do.<br>
    <br>
    [Organizer 1] 11:22:26<br>
    So by increasing the length of the maximum step, if the tolerance is let's say are respected, you can also achieve a faster convergence so that's what I noticed. Those were actually mainly for the integrator changing that max depth i believe and also a little bit by reducing the J2<br>
    <br>
    [Organizer 1] 11:22:43<br>
    That affected the CPU time and so trying to make a little more reasonable.<br>
    <br>
    [Participant 1] 11:22:47<br>
    Yeah. Yeah, I believe so.<br>
    <br>
    [Organizer 1] 11:22:48<br>
    If you have any other issues… feel free to let us know and we can turn it to even try to face it from that point of view. We didn't receive any other emails, I guess, or in the discussion. One of the participants.<br>
    <br>
    [Organizer 1] 11:23:01<br>
    In the discussion forum left that question and you just heard the answer, the one that i gave So I was trying to add in some ways Yeah.<br>
    <br>
    [Participant 1] 11:23:07<br>
    Yeah, the issues I was getting is I think outside of this, it's not really the effect of the propagation configuration, like the step sizes and tolerances, because I actually already tried changing that. I did like a time inspection on like the code that I have<br>
    <br>
    [Participant 1] 11:23:26<br>
    And it's more so the fact of like the initialization of the VM and what you do in each process. It's like It probably is pretty fast in a sequential method. Like you just do the simulation per file ID. But when you start to do multiprocessing, it kind of uh<br>
    <br>
    [Participant 1] 11:23:46<br>
    It definitely lags. And at the beginning it took me in the Codabench, four minutes per simulation or per file ID, which was way too long And then when I tried to make these optimizations in the code, the simulation itself only should have taken, the propagation itself only should have taken 50 seconds.<br>
    <br>
    [Participant 1] 11:24:07<br>
    Profile ID, which is still too long. For the number of files that are there, but I'm just slowly whittling away at the time with ORCID.<br>
    <br>
    [Organizer 1] 11:24:17<br>
    Makes sense. Yeah, yeah.<br>
    <br>
    [Participant 1] 11:24:18<br>
    But yeah, it's too early for me to say really one way or another.<br>
    <br>
    [Participant 1] 11:24:22<br>
    It just does require a lot of work on our side, or I guess my side to try to make the most efficient use of OriKit. Like you said, when you get OriKit, I've actually used OriKit at my work as well.<br>
    <br>
    [Participant 1] 11:24:36<br>
    Actually, just recently i made a I made a software in OriKit to essentially do orbit determination with like GPS data.<br>
    <br>
    [Participant 1] 11:24:44<br>
    As measurements. So even just getting that to work was excruciatingly painful.<br>
    <br>
    [Organizer 1] 11:24:51<br>
    Yeah, you mentioned.<br>
    <br>
    [Participant 1] 11:24:52<br>
    And so like you said, like once you get, OriKit is very powerful. I agree.<br>
    <br>
    [Participant 1] 11:24:57<br>
    But once you get it, only once you get it properly set up, which does take a lot of experimentation and you know, uh.<br>
    <br>
    [Participant 1] 11:25:07<br>
    Like looking into code examples, not necessarily their documentation To get that working.<br>
    <br>
    [Organizer 1] 11:25:14<br>
    Also, I don't know. Yeah, go ahead.<br>
    <br>
    [Participant 1] 11:25:14<br>
    So maybe… I was going to say like, it might not be like it may be too much to ask, but if there was an example of like how to do this propagation, like I know you guys have this example of<br>
    <br>
    [Participant 1] 11:25:29<br>
    The propagation notebook. But if there was this same example, but maybe with like a multi-processed approach then that would also help too.<br>
    <br>
    [Participant 1] 11:25:40<br>
    But actually, what I'll probably do is I'll go and try to run this notebook again and see how long it takes.<br>
    <br>
    [Participant 1] 11:25:45<br>
    And then maybe I'll just rebuild my method from scratch. Using this more directly.<br>
    <br>
    [Participant 1] 11:25:54<br>
    See how that works.<br>
    <br>
    [Organizer 1] 11:25:54<br>
    Yeah. You can also try to post on their forum. They're pretty responsive. I did the same to build the custom atmosphere model you know i'm not a Next.<br>
    <br>
    [Participant 1] 11:26:03<br>
    Oh, and the OriKit. The OriKit one, yeah.<br>
    <br>
    [Organizer 1] 11:26:04<br>
    Yeah, yeah, just post it. I mean, I can try, but honestly, I mean, I can try to more, but… the best way to do it, I mean, since you also use Orchest, so I guess you're also skilled in OriKit probably as much as me, maybe even more than me. So if you're not super successful, I would always suggest go on the Oracle forum and they're usually responsive. So I also did in that way when actually we recorded the<br>
    <br>
    [Participant 1] 11:26:09<br>
    Yeah, I know you guys are busy, so…<br>
    <br>
    [Organizer 1] 11:26:28<br>
    Castle atmosphere model and then I mean, at least they try in a little bit. Then obviously I had to put my time, right? They don't really give you the solution many times, but maybe they know, maybe they tell you which is the best.<br>
    <br>
    [Organizer 1] 11:26:39<br>
    Way to do it, approach it. Maybe they tell you it's a good idea it's a bad idea let's say the different procedure you're doing.<br>
    <br>
    [Participant 1] 11:26:46<br>
    Okay, sounds good. Yeah, I honestly think that everything is there. But if you're saying that if you were able to get three to like three to five seconds per sample, then that's actually fast enough to kind of just run it even sequentially.<br>
    <br>
    [Organizer 1] 11:27:00<br>
    Yeah, that's why.<br>
    <br>
    [Participant 1] 11:27:00<br>
    So I think I'll just like, it's always better to go simple than to go more complicated. So I'll just go back and try to not do multiprocessing and Try to do it sequentially, but make sure that each simulation run does indeed take those three to five seconds and it should be good enough for<br>
    <br>
    [Organizer 1] 11:27:16<br>
    Yes, please. Yes. You should try that. And also let me know. I mean, I can always be mistaken.<br>
    <br>
    [Organizer 1] 11:27:22<br>
    So but at least that's what i found out with my test so yes I have a question for you. When you were mentioning about the score, My question is like, whenever you get a score.<br>
    <br>
    [Organizer 1] 11:27:38<br>
    Do you also input into the leaderboard?<br>
    <br>
    [Participant 1] 11:27:43<br>
    I just, yeah, so like my past few runs, I haven't gotten a score at all.<br>
    <br>
    [Organizer 1] 11:27:44<br>
    Man.<br>
    <br>
    [Participant 1] 11:27:50<br>
    So, but my most recent one, which was like, I think yesterday or two days ago I got a score for the… for the um for the 1.2, but I didn't get a score for the 1.1. So I just didn't submit that, I guess. But I could…<br>
    <br>
    [Participant 1] 11:28:08<br>
    Submit that if you're suggesting to do so.<br>
    <br>
    [Organizer 1] 11:28:11<br>
    So you say you didn't place it inside the leaderboard for the 1.2.<br>
    <br>
    [Organizer 1] 11:28:16<br>
    You do. Okay. I mean, yeah, yeah. I mean, it's always nice since we also send out an email just to, you know.<br>
    <br>
    [Participant 1] 11:28:16<br>
    No, I can do that right now, actually, if you're on it. Yeah, this is what…<br>
    <br>
    [Organizer 1] 11:28:25<br>
    We also send out of, I mean, did you receive the email with like the short feedback and also related to those try to submit the obviously not only submit the models in the sense of<br>
    <br>
    [Organizer 1] 11:28:40<br>
    Trying to work on it but also in the past, I think we mentioned, whenever you have a score, if you can place it in the leaderboard is always good also.<br>
    <br>
    [Participant 1] 11:28:47<br>
    Oh, sure. Yeah, no worries.<br>
    <br>
    [Organizer 1] 11:28:49<br>
    You know make the participant, I don't know, maybe feel more like okay uh we need to work hard. We need to double check, something like that.<br>
    <br>
    [Participant 1] 11:28:56<br>
    Yeah, yeah. Okay. No worries. Yeah, I've been just kind of just focusing on the soft, my, my solution More so to just, I want to get like some numbers. That was my original goal is in the past is to kind of build the entire pipeline from like<br>
    <br>
    [Organizer 1] 11:28:57<br>
    Thank you.<br>
    <br>
    [Organizer 1] 11:29:03<br>
    No worries. No worries.<br>
    <br>
    [Participant 1] 11:29:15<br>
    My solution to Codabench Because it did take some time to kind of debug and see like what was wrong, why wasn't it producing like prediction files and this and that and like what are optimal solutions But I think now that I have like a working pipeline, now it's easier to optimize the whole thing.<br>
    <br>
    [Organizer 1] 11:29:54<br>
    Yeah, yeah.<br>
    <br>
    [Organizer 1] 11:30:00<br>
    Thank you.<br>
    <br>
    [Participant 1] 11:30:02<br>
    But yeah, I'll keep you updated with anything, any questions I have.<br>
    <br>
    [Participant 1] 11:30:06<br>
    And then I'll try to take a look at that survey that you guys sent.<br>
    <br>
    [Participant 1] 11:30:11<br>
    As well. Oh, okay. Awesome.<br>
    <br>
    [Organizer 1] 11:30:11<br>
    Yeah, it's literally just one question. I shouldn't make it more like a point to ever And he really got a few responses. So we're just trying to understand you know um I mean, just start to understand how the participants feel about the model submission, they're having difficulties, not difficulties<br>
    <br>
    [Organizer 1] 11:30:29<br>
    Obviously for a challenge that is on top or whatever the participant who every day.<br>
    <br>
    [Participant 1] 11:30:29<br>
    Yeah.<br>
    <br>
    [Participant 1] 11:30:33<br>
    Oh, what? One thing is I kind of like got it from the example, but it wasn't exactly explicitly stated is that the predictions json is supposed to produce timestamps every 10 minutes from the initial up to three days. Is that correct?<br>
    <br>
    [Organizer 1] 11:30:55<br>
    Let me think. I believe so. I believe so. Yeah, I believe so.<br>
    <br>
    [Participant 1] 11:30:58<br>
    So like you have Yeah, it wasn't exactly like stated that the predictions to JSON has to be Like every 10 minutes apart leading up to three days. I just saw that from the little like snippet there that it's like it's separated by 10 minutes. So I just assumed that<br>
    <br>
    [Organizer 1] 11:31:14<br>
    Yeah, yeah, yeah.<br>
    <br>
        [Participant 1] 11:31:19<br>
    You want prediction values. Every 10 minutes from the initial Plus three days.<br>
    <br>
    [Organizer 1] 11:31:29<br>
    Yeah, I got your point. I think it is correct. I will just double check with Sergio again because he was the one, let's say, preparing the But I will let you i will i will double check and let you know, just confirm. I think it is<br>
    <br>
    [Organizer 1] 11:31:43<br>
    So yes.<br>
    <br>
    [Participant 1] 11:31:44<br>
    Okay, awesome. Thank you. Yeah, I think I'm going to do like a new solution to my problem. My previous one was a little bit strange.<br>
    <br>
    [Participant 1] 11:32:57<br>
    But this is obviously like a different approach. I'm not sure if it'll work. I think it will work.<br>
    <br>
    [Participant 1] 11:33:03<br>
    But we'll see. So, I mean, that's the whole point of this, right? We just like do research and find out.<br>
    <br>
    [Organizer 1] 11:33:05<br>
    Okay. Yeah, yeah, exactly. Yeah, it's very interesting so Yeah, good luck with that.<br>
    <br>
    [Participant 1] 11:33:12<br>
    Cool. Thank you. Yeah, sorry for taking too much time. Yeah, no worries.<br>
    <br>
    [Organizer 1] 11:33:15<br>
    Oh, it's okay for me. I guess if you have any one more question before the end of the session.<br>
    <br>
    [Participant 1] 11:33:23<br>
    That's all I had for now. Maybe I'll join next week and give an update as well.<br>
    <br>
    [Participant 1] 11:33:27<br>
    Because I'm trying to like, because I know we have like a few weeks left. So it's fast approaching for sure.<br>
    <br>
    [Organizer 1] 11:33:33<br>
    Sounds good. Thank you, Atila.<br>
    <br>
    [Participant 1] 11:33:35<br>
    Yep. All right. Thank you. Yeah. Take care. Right.<br>
    <br>
    [Organizer 1] 11:33:38<br>
    Any other question from the other question from Someone else before we close?<br>
    <br>
    [Organizer 1] 11:33:50<br>
    I take it as a no. So, okay. Thank you, everyone, and we're going to meet, I guess, in one week.<br>
    <br>
    [Organizer 1] 11:33:57<br>
    Have a good day. Bye-bye.<br>
    </p>
  </details>
  
</div>
