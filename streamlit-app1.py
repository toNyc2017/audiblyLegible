
import streamlit as st

#import summaries


import os
import sys


# Define your text variables
question_text_tech = """
1. How did the recent conflict between Substack and Twitter emerge, and how was it resolved?
2. What is the business model of Substack, and how does it differ from traditional social media platforms?
3. What is Substack's vision for its platform and its role in the content creation industry?
4. How does Substack view content moderation, and what are its policies regarding freedom of speech and censorship?
5. What is the new feature 'Substack Notes', and how does it contribute to Substack's overall strategy?
6. How is Substack dealing with its current financial situation, including costs exceeding revenues, and what strategies are in place to achieve profitability?
7. What is Substack's stance on the use of open source protocols and user control over their experience on the platform?
"""


# conclusions_text_tech = """Here are some conclusions, assertions, and hypotheses that might be drawn from the conversation:

# 1. **Substack's business model** is providing a unique value proposition to writers, focusing on providing them with a platform to express freely, reach their audience, and monetize their work through a subscription model. This model could revolutionize the content creation industry and pose a significant threat to ad-based platforms.

# 2. **Substack's relationship with Twitter** has been strained due to recent events. Elon Musk's decision to throttle links to Substack, which Twitter later reversed, may suggest potential competitive dynamics or perceived threats between the two platforms.

# 3. The introduction of **Substack Notes**, a feature that allows writers to share short form posts and recommendations, signifies Substack's growth and evolution. This move may also be seen as a direct challenge to social networks like Twitter and Facebook.

# 4. **Content moderation** on Substack presents a challenge, as the platform seeks to balance freedom of speech with the need to maintain a safe, respectful environment. How Substack navigates this will be crucial for its reputation and growth.

# 5. **Substack's financial situation** appears to be a mixed bag. While they have raised substantial capital and claim to have a growing user base, it's mentioned that costs are higher than revenues. This raises questions about Substack's long-term financial sustainability and whether its business model can become profitable at scale.

# 6. **Substack's potential integration with open-source protocols** suggests that the platform is actively looking for ways to enhance user experience and control, which could further differentiate it from competitors.

# 7. Given Substack's recent issues with Twitter, it might be hypothesized that the platform is potentially looking for **alternative ways to grow their user base and increase their mindshare** beyond Twitter.

# 8. The conversation suggests a potential trend of **writers moving towards subscription-based platforms** like Substack, which provide them with greater control over their content and direct engagement with their readers. This could have significant implications for the future of content creation and distribution.

# 9. Substack's goal to create a "new economic engine for culture" suggests the company's aspiration to have a broad societal impact, which may require it to navigate complex issues around freedom of speech, censorship, and content moderation.

# 10. The mention of **Microsoft's AI-powered chatbot** and discussions about AI tech indicates that there's a growing interest and concern about the role of AI in content creation and communication platforms. It might be worth exploring how Substack plans to leverage AI in its platform."

# follow_up_text_tech = "1. **Revenue and profitability**: You mentioned that the costs currently exceed the revenues, which raises concerns about Substack's path to profitability. Could you elaborate on your business model and financial strategies? What are your main revenue streams and cost drivers, and how do you plan to achieve a sustainable balance between the two? 

# 2. **Growth strategy**: Given the recent issues with Twitter, it seems like there might be potential challenges in relying on other social media platforms for user acquisition. What is your strategy for user growth moving forward, and how do you plan to increase your mindshare in the content creator and reader communities independently?

# 3. **Content moderation and user trust**: Striking the right balance between freedom of speech and content moderation is a complex issue. How are you planning to navigate this delicate balance, and what measures are you taking to build trust and ensure user safety without compromising on the freedom of expression? Additionally, how do you plan to handle potential controversies or public relations challenges that may arise due to content moderation issues?
# """

follow_up_text_tech = """
1. **Revenue and profitability**: You mentioned that the costs currently exceed the revenues, which raises concerns about Substack's path to profitability. Could you elaborate on your business model and financial strategies? What are your main revenue streams and cost drivers, and how do you plan to achieve a sustainable balance between the two? 

2. **Growth strategy**: Given the recent issues with Twitter, it seems like there might be potential challenges in relying on other social media platforms for user acquisition. What is your strategy for user growth moving forward, and how do you plan to increase your mindshare in the content creator and reader communities independently?

3. **Content moderation and user trust**: Striking the right balance between freedom of speech and content moderation is a complex issue. How are you planning to navigate this delicate balance, and what measures are you taking to build trust and ensure user safety without compromising on the freedom of expression? Additionally, how do you plan to handle potential controversies or public relations challenges that may arise due to content moderation issues?
"""

#summary_text_tech = summaries.TECH_SUMMARY_1
summary_text_tech = """Chris Best talks to Nilay Patel about the recent drama with Twitter and the launch of Substack Notes.                  Elon Musk's decision to throttle links to Substack publications led to a lot of anger from Substack writers. Twitter later caved and the issue appears to have been resolved. Substack is no longer just an enterprise software vendor but also a consumer product company, which brings with it its own set of content moderation concerns. We also talk about Substack's recent fundraising efforts using a platform called WeFunder.                  In the past two years, Best has learned a lot as the CEO of Substack, and he feels more confident in the story they are telling and in their team. He believes that their mission has been to develop a platform that can help people express themselves
 more freely and that this mission has been successful.                  The part of the story that has changed the most while looking back is what Substack is like. Substack has evolved to become an enterprise software company that provides tools to writers to help them build businesses with their subscription email newsletters. Substack's goal is to create a new economic engine for culture, based on a different business model than ads - subscription-based rather than free content - and to facilitate direct connections between readers and their trusted content creators. The journey has been about tackling a series of concrete steps to get closer to this goal, but we are still early on in this process.                  The vision for Substack is to build a new economic engine for culture by creating a subscription network that allows writers to access a vertically-integrated platform of tools that enable them to compose, publish, and monetize their work in a way that empowers them to take control of their own audience and content.Substack Notes is a new feature that allows writers on Substack to share short form posts and recommendations on the Substack network and help them grow. It draws from ideas from Twitter, Facebook, and other social networks, but the difference is the business model. Substack does not have ads, and instead runs on a paid subscription model, where the readers are the customers.                  Substack was not meant to compete with Twitter, but rather to create an alternative to the attention economy. It is an incentive structure that goes against maximally, cheaply compelling and maximally addictive, and instead focuses on creating content that people find valuable and which they may be willing to pay for. This is in contrast to the other platforms which focus on exploiting their users' attention.                  Sub-stack is not trying to be the "new" Twitter, but they are trying to provide new ways for writers to reach new audiences and to have a comfortable place to share their work.                  Twitter had a good relationship with Sub-Stack before Elon took over. After Elon took over, he put up a warning against Sub-Stack links, throttled posts with Sub-Stack links, and even blocked the word Sub-Stack from being searched. Sub-Stack then announced Notes, a new way for writers to share short-form posts.                  SubStack was shocked by the strong response from Twitter against their launch, as Twitter falsely marked their links as unsafe and tried to throttle the discussion of the word Substack. Elon's claim that SubStack was trying to download a massive portion of the Twitter database is false, and SubStack has not received any answers to their specific questions of what they could do to make the situation better.                  The CEO of Substack experienced Twitter turning off embeds, links, and throttling its API usage, which caused disruption to writers on the platform. He was not given any warning that this was going to happen and was left guessing what was happening. He hopes that what has happened will not happen again and that it will be made clear that this is not the way to handle these kinds of issues. He would like to be able to unpause the API search and make any changes necessary to the way Substack handles these kinds of issues.                  I would love to see Notes be a successful platform for writers to use alongside Twitter and to have conversations, grow their audiences, and share their work. We also discussed the potential implications of Microsoft's AI-powered chatbot and the fears and ambitions people have regarding AI tech. Lastly, we discussed the difficulties of finding directors commentary on streaming services, a movie about BlackBerry, and how technology can be used to make movies.                  Substack is designed to put writers and readers in charge, and its business model is more aligned with writers than other social networks. It is not algorithmic today, but users can still influence the content they see by following the writers they like.                  Substack is an algorithmically based platform that is designed to be in service of the user. It's based off of the choices people are making, such as who they are subscribing to and what they like. Substack is interested in ways to help content spread as frictionlessly as possible, but they do not have a specific plan with any of the decentralization protocols like ActivityPub or Blue Sky.                  The team has not made any decisions on how to incorporate open source protocols into their product, but they have discussed the idea. They have been exploring the idea of how to give users more control and freedom while still providing them with an easy-to-use platform. They are interested in the idea of allowing users to have more control over their experience, but have not settled on any one answer yet.                  I worry sometimes that people take the leap of assuming a trustless system is the answer to all their problems, but a better solution is to have a platform they can trust. Substack has set up a system of trust by allowing users to take their relationships and payment relationships with them when they leave. Despite the fact that Substack Notes is closed, it is still based on the same subscription network and users can go and take their audience with them.                  SubStack is a subscription network and the subscription graph is the thing that sets it apart from other services. It is what writers want and what will enable them to get paid. The court case involving Blurred Lines and Marvin Gaye has had huge implications for the music industry and is the reason why Ed Sheeran was recently in court.                  Chris and I discussed Substack's content moderation guidelines for its new consumer feature, Substack Notes. I mentioned Ben Thompson's post on moderation guidelines and mentioned my mistake in using a controversial example that was not clear enough. I asked Chris whether the feature was inheriting the expectations from consumer platforms, like Twitter, to moderate content to a higher degree than it previously had.                  We are trying to build a subscription network, which is different from social networking and enterprise software. Our focus is on moderation instead of censorship and we believe that this will make something better than what has been before.                  Substack notes is committed to freedom of speech and a free society, and they are working to design the network in a way that allows people to be in control of their own experience. They are still in the early stages of figuring out how to navigate content moderation and are not going to engage in "gotcha" content moderation questions.                  No, we should not allow overt racism on Substack. Our terms of service have been clear on this matter and we do not think that censorship of bad ideas is the most effective way to combat them. We have seen over the past several years that censorship does not build trust, end polarization, or prevent the spread of bad ideas, and so we believe it is not a successful tool in this regard.                  Sub-stack does not support government censorship and believes in the promotion of freedom of the press and freedom of speech. They are working hard to make sub-stack a great place for readers and writers, and look at it as an index fund of culture that is not the place for anyone.                  Substack has a team dedicated to trust and safety, and handles any copyright infringement claims through the DMCA process. They use a combination of automated and manual systems to ensure that content remains in compliance with their terms of service.                  We raised a lot of money, used it to kick-start the network, and it worked. We've created a powerful, growing community and have deterred our competitors. However, the costs are higher than the revenues, and we've had to use other methods (like a retail investor program) to stay afloat.                  Substack has over 35 million active subscriptions, and the top 10 publishers are making a collective $25 million per year. Investment in Substack is a regulated community funding process, and the financial information associated with that process has been given to potential investors. Returns on investment are not something that can be commented on.                  Substack has a business model which works - they make money when writers make money and they are growing, on a path to profitability. They don't rely heavily on Twitter, though they do leverage it for mindshare, and they are looking to the app to grow their user base.
"""

##################################################################

question_text_fin = """
1. What is the projected growth of the U.S. wealth management industry and the anticipated allocation to alternative investments by 2030?
2. How are top alternative asset managers responding to the growing demand for alternative investments from financial advisors?
3. How is the end of financial repression, caused by the zero bound in an era of quantitative easing, influencing the shift from traditional assets to alternative investments?
4. How have the evolution of asset management over the past 30 years and the demands of high net worth clients influenced the growth of alternative investments?
5. What are the key traits of asset management firms that are successfully tapping into the wealth management channel for alternative investments?
6. How are hedge funds and other alternative investments being positioned to retail investors, and what are the perceived benefits of these investments?
7. What role does education play in promoting understanding and adoption of alternative investments among financial advisors and their clients?
"""


follow_up_text_fin = """
1. **Client Demographics:** What is the demographic profile of the clients showing an increased interest in alternative investments? Are these primarily high-net-worth individuals or is the interest broad-based across different wealth segments? This could provide insight into the potential growth and scale of the alternative investments market.

2. **Educational Initiatives:** What specific educational initiatives are being put in place to ensure that advisors and their clients understand the risks and benefits of alternative investments? How are these initiatives being received, and are they effectively increasing understanding and comfort with these types of investments?

3. **Regulatory Impact:** How might future regulatory changes impact the growth and accessibility of alternative investments? Are there anticipated challenges or risks that could result from these changes, and how are asset managers and financial advisors preparing for these potential shifts?

"""

conclusions_text_tech = """
1. **Substack's business model** is providing a unique value proposition to writers, focusing on providing them with a platform to express freely, reach their audience, and monetize their work through a subscription model. This model could revolutionize the content creation industry and pose a significant threat to ad-based platforms.

2. **Substack's relationship with Twitter** has been strained due to recent events. Elon Musk's decision to throttle links to Substack, which Twitter later reversed, may suggest potential competitive dynamics or perceived threats between the two platforms.

3. The introduction of **Substack Notes**, a feature that allows writers to share short form posts and recommendations, signifies Substack's growth and evolution. This move may also be seen as a direct challenge to social networks like Twitter and Facebook.

4. **Content moderation** on Substack presents a challenge, as the platform seeks to balance freedom of speech with the need to maintain a safe, respectful environment. How Substack navigates this will be crucial for its reputation and growth.

5. **Substack's financial situation** appears to be a mixed bag. While they have raised substantial capital and claim to have a growing user base, it's mentioned that costs are higher than revenues. This raises questions about Substack's long-term financial sustainability and whether its business model can become profitable at scale.

6. **Substack's potential integration with open-source protocols** suggests that the platform is actively looking for ways to enhance user experience and control, which could further differentiate it from competitors.

7. Given Substack's recent issues with Twitter, it might be hypothesized that the platform is potentially looking for **alternative ways to grow their user base and increase their mindshare** beyond Twitter.

8. The conversation suggests a potential trend of **writers moving towards subscription-based platforms** like Substack, which provide them with greater control over their content and direct engagement with their readers. This could have significant implications for the future of content creation and distribution.

9. Substack's goal to create a "new economic engine for culture" suggests the company's aspiration to have a broad societal impact, which may require it to navigate complex issues around freedom of speech, censorship, and content moderation.

10. The mention of **Microsoft's AI-powered chatbot** and discussions about AI tech indicates that there's a growing interest and concern about the role of AI in content creation and communication platforms. It might be worth exploring how Substack plans to leverage AI in its platform.
"""


conclusions_text_fin = """
1. **Increasing Interest in Alternative Investments:** There is a notable increase in interest from financial advisors and their clients towards alternative investments. This is driven by the search for better returns, more predictability, and lower volatility compared to traditional assets. Allocations to alternative investments are projected to rise significantly in the next decade. 
2. **Technological Innovation and Accessibility:** Technological advances and regulatory changes are making alternative investments more accessible to a wider range of investors. Platforms like CASE are playing a pivotal role in bridging the gap between alternative asset managers and independent advisors.
3. **Education is Crucial:** There is a strong emphasis on the importance of education in understanding alternative investments. For many advisors and their clients, this is a new area, and understanding the associated risks and benefits is crucial. 
4. **Institutional Shift Towards Retail:** Large institutional firms, such as Blackstone, are now looking towards the retail market for growth. This is due to saturation in the institutional market, and the realization of untapped potential within retail investors. 
5. **Potential Risk of Mis-selling and Lack of Diligence:** There are potential risks associated with alternative investments, such as lack of research, diligence, and the potential for mis-selling. Understanding the strategy behind the investment and the specific risks associated with each alternative asset is necessary.
6. **Regulatory Changes and Impact:** The SEC has relaxed accreditation rules, making it easier for more people to access alternative investments. However, there is concern about the quality of some of the products that have resulted from these changes. 
7. **Shift in Asset Allocation Strategies:** There is a predicted shift in asset allocation strategies from traditional indexing towards a higher percentage allocation to alternative investments. This is influenced by market conditions, including the end of financial repression caused by the zero bound in an era of quantitative easing.
8. **Demand for Better Products:** Wealth management advisors are seeking products with lower minimums and greater scalability that can provide better returns than traditional asset allocation strategies (e.g., 60-40 equity-bond split).
9. **Trend Towards Private Assets and Credit:** Private assets, including private credit, have gained popularity due to their performance and the diversification they offer. They're seen as a beneficial addition to portfolios, not just as equity substitutes.
10. **Macro Trends Influencing the Shift:** Global uncertainty, political polarization, and central bank liquidity have contributed to the shift towards alternative investments.
"""







#summary_text_fin = summaries.FIN_SUMMARY_1

summary_text_fin = """"The alt industry is changing as financial advisors seek greater access to alternative investments to better serve their clients. Currently, the United States wealth management industry is a 40 trillion industry, with allocations to alternative investments at 3-5 percent. However, this is expected to increase to $60 trillion by 2030, with a potential $5-10 trillion reallocation over the next decade into alternatives. In response, some of the world's top alternative asset managers are partnering with independent advisors and CASE, the leading alternative investment platform, is seeking to bridge the gap between them. Technology and demand for alternatives is transforming wealth management."
"Asset managers are rapidly positioning their firms to take advantage of the wealth available from alternative investments. There has historically been a lack of access to these investments, but platforms like Case have made it easier to invest, resulting in a large influx of capital from traditional assets into alternative investments. The average retail account is only allocated around 3-4% to these investments, often in daily liquid products which are subpar compared to LP world private assets and hedge funds. The catalyst for this shift is the end of financial repression caused by the zero bound in an era of quantitative easing, as indexing in the equity side has been a successful strategy for asset allocators."
"Indexing of public equity has no choice but to overpay if multiple elevation is a problem, and suggests that the opportunity set for alternatives is not just going from 4 to 7 percent, but from 4 to 30 percent. It also mentions that the people on the institutional side are looking at valuations and private equity and the flood of capital on the sidelines and venture capital, and that the argument of forward-looking returns not looking as attractive is true of any risk asset. The text suggests that disciplined private equity buyers are the ones who will not overpay egregiously."
"The retail world has seen an evolution in asset management over the past 30 years, starting with David Swenson's balanced portfolio and shifting to alternatives such as hedge funds, private assets, and real estate. High net worth clients have been demanding better returns, more predictability, and lower volatility, and private assets have outperformed everything. Institutional retirement funds have saturated the institutional market, and alternative firms are now looking to retail for growth. Blackstone has done this well, and products are now being made available to retail investors. The biggest trend in institutional asset management is private credit, which is quickly being adopted by retail."
"This text is about the growth of alternative investments in the retail space, which has been taking place for the past five years. It discusses how asset managers have been trying to explain the potential of alternative investments to investors for the past decade and how firms that are willing to commit to bringing product into the wealth management channel are the ones that are winning. It also mentions that firms that are successful in wealth management need to have commitment from the top, dedicate separate resources to it, and understand the needs of the customer."
"David Bonson is looking for a product with lower minimums and scalability across 200 clients that can provide better returns than the 60-40. Wealth management advisors have become more sophisticated and have access to technology and information that can help them use alternative products. Matt and David are discussing how large managers such as Blackstone and Apollo benefit from the current industry circumstances."
"Hedge funds have been on wealth platforms for around 10 years, with the big firms leading the way. Smaller and medium-sized firms then followed. Private assets have outperformed hedge funds in the past decade, and they are seen as a diversifier rather than an equity substitute. Hedge funds provide an illiquidity premium, a scale premium, and no regular valuation marks, which creates a smoother return pattern. When having a conversation with a client who has no money in alternatives, the initial educational conversation is about the benefits of investing in alternatives."
"The text discusses the importance of alternatives for clients, and how they can be used to capture risk premium and produce non-correlated streams of return. It also mentions the need for education when it comes to investing in alternatives, as this was found to be the number one barrier for advisors when surveyed."
"There is a real need for financial advisors to become educated in alternative investments and strategies, as a large amount of capital is moving into the space. It also notes that the recent 14 year bull equity market and 40 year bull rates market have warped people's perspectives, and that central bank liquidity has been a large factor in the unusual market environment. It emphasizes the need for education in order to understand the current market environment and how to use alternative investments."
"Hedge funds and alternative investments have become easier to access due to advances in technology and regulatory changes. It also mentions how current events, such as global uncertainty and political polarization, have caused more money to flow into macro strategies, hard asset strategies, and opportunity zones."
"Alternative investments are becoming increasingly popular among financial advisors, with more and more RIAs onboarding and controlling between 1.1 and $1.4 trillion in assets. This shift is happening quickly, with first-time users of platforms buying alts more than two to three times per day. Additionally, wealth platforms are offering direct deals from private equity funds to larger clients, which is a new trend in institutional asset management. Despite the influx of money and people taking advantage of it, it is important to not invest in alternatives without proper research."
"Risks associated with alternative investments are disucssed, such as manager diligence, execution, and strategy proficiency. It is suggested that asset allocators have chosen passive long only investments due to the lack of research and diligence required. The text also suggests that alternative investments can have idiosyncratic risks, and that asset managers and financial advisors should approach alternative investments as a solution rather than a single fund with a single track record."
"They also discuss the importance of working with financial advisors when investing in alternative investments and the risks associated with not doing so. It also mentions the importance of understanding the strategy behind the investment and the risks associated with mis-selling, not educating properly, and funds becoming too large. Finally, it mentions the role of the SEC in this conversation."
"The SEC has relaxed their accreditation rules to be more inclusive and allow more people to access alternative investments. This is being driven by macro trends such as technology, advisor demand, and manager innovation. The SEC initially had good intentions, but their execution was poor as they created a big industry around daily alts, daily NAV, which were subpar products. The advice for those looking to take advantage of the gold rush is to understand that risk is more than just liquidity and to provide appropriate solutions to investors."

"""



def main():
    st.title("Audible Insights Made Legible")

    
    
    st.header("SALT Conference discussion of Alternative Investments")
    #st.text_area("Questions Addressed", question_text_fin,height=300)
     

    with st.container():
        st.write("---")
        st.markdown("**Questions Addressed**", unsafe_allow_html=True)
        st.markdown(question_text_fin, unsafe_allow_html=True)
        st.write("---")

    with st.container():
        st.write("---")
        st.markdown("**Conclusions Possible From This Text**", unsafe_allow_html=True)
        st.markdown(conclusions_text_fin, unsafe_allow_html=True)
        st.write("---")


    with st.container():
        st.write("---")
        st.markdown("**Implied Follow Up Questions**", unsafe_allow_html=True)
        st.markdown(follow_up_text_fin, unsafe_allow_html=True)
        st.write("---")

    with st.container():
        st.write("---")
        st.markdown("**Summary of Text**", unsafe_allow_html=True)
        st.markdown(summary_text_fin, unsafe_allow_html=True)
        st.write("---")
   
  
   
##############################################################################################################

  
    
    
    st.header("Decoder interview between Nilay Patel and Substack CEO Chris Best")
    #st.text_area("**Questions Addressed**", question_text_tech, height=300)
    


    with st.container():
        st.write("---")
        st.markdown("**Questions Addressed**", unsafe_allow_html=True)
        st.markdown(question_text_tech, unsafe_allow_html=True)
        st.write("---")

    with st.container():
        st.write("---")
        st.markdown("**Conclusions Possible From This Text**", unsafe_allow_html=True)
        st.markdown(conclusions_text_tech, unsafe_allow_html=True)
        st.write("---")


    with st.container():
        st.write("---")
        st.markdown("**Implied Follow Up Questions**", unsafe_allow_html=True)
        st.markdown(follow_up_text_tech, unsafe_allow_html=True)
        st.write("---")

    with st.container():
        st.write("---")
        st.markdown("**Summary of Text**", unsafe_allow_html=True)
        st.markdown(summary_text_tech, unsafe_allow_html=True)
        st.write("---")

 
if __name__ == "__main__":
    main()
