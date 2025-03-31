import streamlit as st
from dataclasses import dataclass
from typing import List

st.set_page_config(
    page_title="Conservation Economics Mock Test",
    page_icon="solar.jpg", 
    layout="centered"
)

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] li:first-child {
            display: none;
        }
    
        /* Capitalize each entry in the sidebar */
        [data-testid="stSidebarNav"] span {
            text-transform: capitalize;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

@dataclass
class Question:
    text: str
    options: List[str]
    correct_answer: str

def create_footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            color: black;
            text-align: center;
            padding: 10px 0;
        }
        .footer a {
            color: #007bff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            Created by <a href="https://www.linkedin.com/in/ankitverma2405/" target="_blank">Ankit Verma (aka Solar System)</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.title("Conservation Economics Mock Test")
    st.header("Feature Coming Soon!")
    
#     MOCK_TEST_QUESTIONS = [
#         # Week 0
# Question(
# "The ability to produce a good at a lower opportunity cost than another producer is a definition of",
# ["real advantage", "monetary advantage", "comparative advantage", "opportunity advantage"],
# "comparative advantage"
# ),
# Question(
# "Fluctuations in economic activity, such as employment and production, are referred to as",
# ["business cycles", "economic cycles", "production cycles", "market cycles"],
# "business cycles"
# ),
# Question(
# "The property of society getting the most it can from its scarce resources is a definition of",
# ["efficiency", "equality", "prudence", "sustainability"],
# "efficiency"
# ),
# Question(
# "In the word root for Economics, 'nemein' stands for",
# ["together", "to keep", "house", "manage"],
# "manage"
# ),
# Question(
# "Whatever must be given up to obtain some item is a definition of",
# ["explicit costs", "implicit costs", "opportunity costs", "phantom costs"],
# "opportunity costs"
# ),
# Question(
# "Rational decision making compares",
# ["average benefits to average costs", "average benefits to marginal costs", "marginal benefits to average costs", "marginal benefits to marginal costs"],
# "marginal benefits to marginal costs"
# ),
# Question(
# "Something that induces a person to act is a definition of",
# ["enticement", "attraction", "incentive", "occupation"],
# "incentive"
# ),
# Question(
# "Input costs that require an outlay of money are",
# ["explicit costs", "implicit costs", "opportunity costs", "phantom costs"],
# "explicit costs"
# ),
# Question(
# "The property of distributing economic prosperity uniformly among the members of society is a definition of",
# ["efficiency", "equality", "prudence", "sustainability"],
# "equality"
# ),
# Question(
# "The ability of an individual to own and exercise control over scarce resources is known as",
# ["property rights", "resource rights", "individual rights", "social rights"],
# "property rights"
# ),
        
#         # Week 1
# Question(
# "In the word root for conservation, 'con' stands for",
# ["together", "to keep", "house", "manage"],
# "together"
# ),
# Question(
# "The ability of a single economic actor (or small group of actors) to have a substantial influence on market prices is known as",
# ["price power", "market power", "externality", "economic power"],
# "market power"
# ),
# Question(
# "An economy that allocates resources through the decentralized decisions of many firms and households as they interact in markets for goods and services is a/an",
# ["urban economy", "rural economy", "planned economy", "market economy"],
# "market economy"
# ),
# Question(
# "In the word root for conservation, 'servare' stands for",
# ["together", "to keep", "house", "manage"],
# "to keep"
# ),
# Question(
# "Which of these is true?",
# ["Wants are unlimited, resources are unlimited", "Wants are limited, resources are limited", "Wants are unlimited, resources are limited", "Wants are limited, resources are unlimited"],
# "Wants are unlimited, resources are limited"
# ),
# Question(
# "An increase in the overall level of prices in the economy is",
# ["inflation", "deflation", "stagflation", "priceflation"],
# "inflation"
# ),
# Question(
# "The Phillips curve shows the relation between",
# ["profit and loss", "marked price and selling price", "inflation rate and unemployment rate", "electricity consumption and heat output"],
# "inflation rate and unemployment rate"
# ),
# Question(
# "In the word root for Economics, 'oikos' stands for",
# ["together", "to keep", "house", "manage"],
# "house"
# ),
# Question(
# "Most of rational thinking occurs",
# ["before the margin", "at the margin", "after the margin", "none of these"],
# "at the margin"
# ),
# Question(
# "Input costs that do not require an outlay of money are",
# ["explicit costs", "implicit costs", "opportunity costs", "phantom costs"],
# "implicit costs"
# ),
        
#         # Week 2
# Question(
# "Which of these is not a pillar of sustainability?",
# ["environmental sustainability", "economic sustainability", "trans-boundary sustainability", "social sustainability"],
# "trans-boundary sustainability"
# ),
# Question(
# "The Trinity explosion of 1945 is taken as the beginning of the",
# ["Holocene", "Cenocene", "Anthropocene", "Eocene"],
# "Anthropocene"
# ),
# Question(
# "According to the Malthusian model,",
# [
# "Population grows in geometric progression, food supply increases in arithmetic progression",
# "Population grows in geometric progression, food supply increases in geometric progression",
# "Population grows in arithmetic progression, food supply increases in arithmetic progression",
# "Population grows in arithmetic progression, food supply increases in geometric progression"
# ],
# "Population grows in geometric progression, food supply increases in arithmetic progression"
# ),
# Question(
# "The demographic transition sees a society move from",
# [
# "high birth rate, low death rate to low birth rate, high death rate",
# "low birth rate, high death rate to low birth rate, low death rate",
# "high birth rate, high death rate to low birth rate, low death rate",
# "high birth rate, high death rate to low birth rate, high death rate"
# ],
# "high birth rate, high death rate to low birth rate, low death rate"
# ),
# Question(
# "Which of these is a pillar of sustainability?",
# ["social sustainability", "industrial sustainability", "agricultural sustainability", "trans-boundary sustainability"],
# "social sustainability"
# ),
# Question(
# "Which of these is a preventive check according to Malthus?",
# ["foresight", "vice", "misery", "flood"],
# "foresight"
# ),
# Question(
# "The quantum of human impacts can be written as",
# ["I = P + A + T", "I = P X A + T", "I = P X A X T", "I = P + A X T"],
# "I = P X A X T"
# ),
# Question(
# "The book 'An Essay on the Principle of Population' was written by",
# ["Darwin", "Malthus", "Spencer", "Owens"],
# "Malthus"
# ),
# Question(
# "The logistic growth equation curve is",
# ["I-shaped", "J-shaped", "S-shaped", "U-shaped"],
# "S-shaped"
# ),
# Question(
# "Which of these is a positive check according to Malthus?",
# ["late marriage", "war", "celibacy", "moral restraint"],
# "war"
# ),

#         # Week 3
# Question(
# "___ is used to identify which potential impacts are relevant to assess. (Fill in the blank)",
# ["screening", "scoping", "reporting", "review"],
# "scoping"
# ),
# Question(
# "The potential or capacity of a material to have adverse effects on living organisms is",
# ["vulnerability", "susceptibility", "sustainability", "toxicity"],
# "toxicity"
# ),
# Question(
# "A deciduous forest in Madhya Pradesh was converted to a mine. After the mining operations were over, the pits were filled up with soil and species of deciduous forest planted again. This is an example of",
# ["recovery", "restoration", "enhancement", "replacement"],
# "restoration"
# ),
# Question(
# "Hydrocarbons derived from incomplete burning of mineral oils are",
# ["petrogenic hydrocarbons", "pyrogenic hydrocarbons", "biogenic hydrocarbons", "chemoenic hydrocarbons"],
# "pyrogenic hydrocarbons"
# ),
# Question(
# "A deciduous forest in Madhya Pradesh was converted to a mine. After the mining operations were over, the pits were filled up with water and a lake was created. It is now visited by several migratory birds. This is an example of",
# ["recovery", "restoration", "enhancement", "replacement"],
# "replacement"
# ),
# Question(
# "The relative effect of exposure is",
# ["vulnerability", "sensitivity", "sustainability", "toxicity"],
# "sensitivity"
# ),
# Question(
# "___ determines which projects or developments require a full or partial impact assessment study. (Fill in the blank)",
# ["screening", "scoping", "reporting", "review"],
# "screening"
# ),
# Question(
# "The extent to which a chemical is available for uptake into an organism is",
# ["bioavailability", "bioaccumulation", "biomagnification", "bioresponse"],
# "bioavailability"
# ),
# Question(
# "Hydrocarbons derived from biological processes acting on mineral oils are",
# ["petrogenic hydrocarbons", "pyrogenic hydrocarbons", "biogenic hydrocarbons", "chemoenic hydrocarbons"],
# "biogenic hydrocarbons"
# ),
# Question(
# "Any changes in natural or human systems that inadvertently increase vulnerability to climatic stimuli; an adaptation that does not succeed in reducing vulnerability but increases it instead is a definition for",
# ["adaptation", "mitigation", "maladaptation", "malmitigation"],
# "maladaptation"
# ),

#         # Week 4
# Question(
# "Which of these is a deterministic factor?",
# ["environmental variation", "forest fire", "death rate", "diseases"],
# "death rate"
# ),
# Question(
# "I tried growing vegetables under my teak plantation, but the vegetable plants died out. I should be concerned about",
# ["autophagy", "allelophagy", "autopathy", "allelopathy"],
# "allelopathy"
# ),
# Question(
# "The movement of lions across the Gir landscape is an example of",
# ["diffusion", "secular dispersal", "jump dispersal", "drifting"],
# "diffusion"
# ),
# Question(
# "'The geographical distribution of a species will be controlled by that environmental factor for which the organism has the narrowest range of tolerance.' This is the statement for",
# ["Liebig's law of the minimum", "Liebig's law of the maximum", "Shelford's law of tolerance", "Shelford's law of intolerance"],
# "Shelford's law of tolerance"
# ),
# Question(
# "The regular, seasonal movement of animals, often along fixed routes is called",
# ["translocation", "migration", "dispersal", "drifting"],
# "migration"
# ),
# Question(
# "Which of these is a stochastic factor?",
# ["birth rate", "death rate", "population structure", "environmental fluctuation"],
# "environmental fluctuation"
# ),
# Question(
# "The movement of individuals away from their place of birth or hatching or seed production into a new habitat or area to survive and reproduce is called",
# ["translocation", "migration", "dispersal", "drifting"],
# "dispersal"
# ),
# Question(
# "Scarcity of food is a",
# ["chemical factor", "demographic factor", "push factor", "pull factor"],
# "push factor"
# ),
# Question(
# "Which of these correctly represents the process of habitat fragmentation and loss?",
# [
# "Original forest → Dissection → Perforation → Fragmentation → Attrition",
# "Original forest → Dissection → Attrition → Fragmentation → Perforation",
# "Original forest → Dissection → Perforation → Attrition → Fragmentation",
# "Original forest → Dissection → Fragmentation → Perforation → Attrition"
# ],
# "Original forest → Dissection → Perforation → Fragmentation → Attrition"
# ),
# Question(
# "A root zone treatment plant is an example of",
# ["phytoremediation", "biological control", "biomagnification", "bioaccumulation"],
# "phytoremediation"
# ),
        
#         # Week 5
# Question(
# "A measure of the responsiveness of quantity demanded or quantity supplied to a change in one of its determinants is",
# ["elasticity", "responsivity", "demand-supply equilibrium", "pricing"],
# "elasticity"
# ),
# Question(
# "The ability to produce a good using fewer inputs than another producer is",
# ["comparative advantage", "absolute advantage", "production advantage", "resource advantage"],
# "absolute advantage"
# ),
# Question(
# "Common resource goods are",
# [
# "excludable, rival in consumption",
# "non-excludable, rival in consumption",
# "excludable, non-rival in consumption",
# "non-excludable, non-rival in consumption"
# ],
# "non-excludable, rival in consumption"
# ),
# Question(
# "If private parties can bargain without cost over the allocation of resources, they can solve the problem of externalities on their own. This is a statement for",
# ["Allocation theorem", "Phillips theorem", "Coase theorem", "Nash theorem"],
# "Coase theorem"
# ),
# Question(
# "Development that meets the needs of the present without compromising the ability of future generations to meet their own needs is known as",
# ["Good development", "Sustainable development", "Futuristic development", "Gandhian development"],
# "Sustainable development"
# ),
# Question(
# "Club goods are",
# [
# "excludable, rival in consumption",
# "non-excludable, rival in consumption",
# "excludable, non-rival in consumption",
# "non-excludable, non-rival in consumption"
# ],
# "excludable, non-rival in consumption"
# ),
# Question(
# "Which of these is not a method of internalisation of externalities?",
# ["tradable pollution permits", "charities to social causes", "command-and-control policies", "free market"],
# "free market"
# ),
# Question(
# "Private goods are",
# [
# "excludable, rival in consumption",
# "non-excludable, rival in consumption",
# "excludable, non-rival in consumption",
# "non-excludable, non-rival in consumption"
# ],
# "excludable, rival in consumption"
# ),
# Question(
# "A simplified description, especially a mathematical one, of a system or process, to assist calculations and predictions is the definition of a / an",
# ["equation", "model", "philosophy", "process dynamics"],
# "model"
# ),
# Question(
# "The impact of one person's actions on the well-being of a bystander is",
# ["actor-observer effect", "externality", "internality", "benefits principle"],
# "externality"
# ),
        
#         # Week 6
# Question(
# "The claim that, other things being equal, the quantity demanded of a good falls when the price of the good rises is a statement of",
# ["law of demand", "law of supply", "law of quantity demanded", "law of quantity supplied"],
# "law of demand"
# ),
# Question(
# "A legal maximum on the price at which a good can be sold is",
# ["price ceiling", "price floor", "selling ceiling", "selling floor"],
# "price ceiling"
# ),
# Question(
# "A good for which, other things being equal, an increase in income leads to a decrease in demand is",
# ["normal good", "inferior good", "Giffen good", "common good"],
# "inferior good"
# ),
# Question(
# "A table that shows the relationship between the price of a good and the quantity supplied is",
# ["demand table", "demand schedule", "supply table", "supply schedule"],
# "supply schedule"
# ),
# Question(
# "A graph of the relationship between the price of a good and the quantity demanded is",
# ["demand curve", "supply curve", "Laffer's curve", "Phillips curve"],
# "demand curve"
# ),
# Question(
# "A table that shows the relationship between the price of a good and the quantity demanded is",
# ["demand table", "demand schedule", "supply table", "supply schedule"],
# "demand schedule"
# ),
# Question(
# "A measure of how much the quantity demanded of one good responds to a change in the price of another good, computed as the percentage change in quantity demanded of the first good divided by the percentage change in price of the second good is",
# ["price elasticity of demand", "income elasticity of demand", "cross-price elasticity of demand", "price elasticity of supply"],
# "cross-price elasticity of demand"
# ),
# Question(
# "Rice and wheat are",
# ["substitutes", "complements", "club goods", "public goods"],
# "substitutes"
# ),
# Question(
# "A good for which, other things being equal, an increase in income leads to an increase in demand is",
# ["normal good", "inferior good", "Giffen good", "common good"],
# "normal good"
# ),
# Question(
# "A measure of how much the quantity demanded of a good responds to a change in the price of that good, computed as the percentage change in quantity demanded divided by the percentage change in price is",
# ["price elasticity of demand", "income elasticity of demand", "cross-price elasticity of demand", "price elasticity of supply"],
# "price elasticity of demand"
# ),
        
#         # Week 7
# Question(
# "The price of a good that prevails in the world market for that good is the definition of",
# ["export price", "import price", "world price", "domestic price"],
# "world price"
# ),
# Question(
# "The area between the demand curve and the price is an indicator of",
# ["consumer surplus", "producer surplus", "total surplus", "deadweight loss"],
# "consumer surplus"
# ),
# Question(
# "The amount a buyer is willing to pay for a good minus the amount the buyer actually pays for it is",
# ["consumer surplus", "producer surplus", "total surplus", "deadweight loss"],
# "consumer surplus"
# ),
# Question(
# "The amount a seller is paid for a good minus the seller’s cost of providing it is",
# ["consumer surplus", "producer surplus", "total surplus", "deadweight loss"],
# "producer surplus"
# ),
# Question(
# "Value to buyers minus Cost to sellers is",
# ["consumer surplus", "producer surplus", "total surplus", "deadweight loss"],
# "total surplus"
# ),
# Question(
# "The fall in total surplus that results from a market distortion, such as a tax is",
# ["consumer surplus", "producer surplus", "total surplus", "deadweight loss"],
# "deadweight loss"
# ),
# Question(
# "Laffer's curve represents the relationship between",
# ["inflation and unemployment", "tax size and tax revenue", "producer surplus and consumer surplus", "tax size and deadweight loss"],
# "tax size and tax revenue"
# ),
# Question(
# "Imposition of a tariff",
# ["increases producer surplus and government revenue", 
# "increases consumer surplus and government revenue", 
# "increases producer surplus, consumer surplus, and government revenue", 
# "increases total surplus"
# ],
# "increases producer surplus and government revenue"
# ),

# Question(
# "The maximum amount that a buyer will pay for a good is",
# ["willingness to pay", "market demand", "demand curve", "buyer's surplus"],
# "willingness to pay"
# ),

# Question(
# "The area between the supply curve and the price is an indicator of",
# ["consumer surplus", "producer surplus", "total surplus", "deadweight loss"],
# "producer surplus"
# ),
        
#         # Week 8
# Question(
# "For a positive consumption externality, which of the following is correct?",
# ["SMB = PMB", "SMB = PMB - MD", "SMB = PMB + MB", "SMC = PMC / MD"],
# "SMB = PMB + MB"
# ),
# Question(
# "For a positive production externality, which of the following is correct?",
# ["SMB = PMB", "SMB = PMB - MD", "SMB = PMB + MB", "SMC = PMC / MD"],
# "SMB = PMB"
# ),
# Question(
# "The direct cost to producers of producing an additional unit of a good is called",
# ["private marginal cost (PMC)", "social marginal cost (SMC)", "private marginal benefit (PMB)", "social marginal benefit (SMB)"],
# "private marginal cost (PMC)"
# ),
# Question(
# "For a negative production externality, which of the following is correct?",
# ["SMC = PMC + MD", "SMC = PMC - MD", "SMC = PMC", "SMC = PMC - MB"],
# "SMC = PMC + MD"
# ),
# Question(
# "The private marginal cost to producers plus any costs associated with the production of the good that are imposed on others is called",
# ["private marginal cost (PMC)", "social marginal cost (SMC)", "private marginal benefit (PMB)", "social marginal benefit (SMB)"],
# "social marginal cost (SMC)"
# ),
# Question(
# "Partying with loud noise is an example of",
# ["negative production externality", "positive production externality", "negative consumption externality", "positive consumption externality"],
# "negative consumption externality"
# ),
# Question(
# "When an individual's consumption increases the well-being of others, but the individual is not compensated by those others, this is an example of",
# ["negative production externality", "positive production externality", "negative consumption externality", "positive consumption externality"],
# "positive consumption externality"
# ),
# Question(
# "When a firm's production increases the well-being of others but the firm is not compensated by those others, this is an example of",
# ["negative production externality", "positive production externality", "negative consumption externality", "positive consumption externality"],
# "positive production externality"
# ),
# Question(
# "When an individual's consumption reduces the well-being of others who are not compensated by the individual, this is an example of",
# ["negative production externality", "positive production externality", "negative consumption externality", "positive consumption externality"],
# "negative consumption externality"
# ),
# Question(
# "For a negative consumption externality, which of the following is correct?",
# ["SMB = PMB", "SMB = PMB - MD", "SMB = PMB + MB", "SMC = PMC / MD"],
# "SMB = PMB - MD"
# ),

#         # Week 9
# Question(
# "Costs that have already been committed and cannot be recovered are called",
# ["fixed costs", "variable costs", "marginal costs", "sunk costs"],
# "sunk costs"
# ),
# Question(
# "Total revenue minus total cost, including both explicit and implicit costs, is a definition of",
# ["economic profit", "accounting profit", "profit", "loss"],
# "economic profit"
# ),
# Question(
# "The increase in total cost that arises from an extra unit of production is called",
# ["fixed costs", "variable costs", "marginal costs", "sunk costs"],
# "marginal costs"
# ),
# Question(
# "A monopolist firm's profit is given by which formula?",
# ["(Price - ATC) x Q", "(Price - Q) x ATC", "(ATC - Q) x Price", "Price x Q - ATC"],
# "(Price - ATC) x Q"
# ),
# Question(
# "Which of the following is true for a competitive firm?",
# ["P > MR", "P > MC", "MR > MC", "MR = MC"],
# "MR = MC"
# ),
# Question(
# "The amount a firm receives for the sale of its output is defined as",
# ["total revenue", "total cost", "profit", "loss"],
# "total revenue"
# ),
# Question(
# "When the cost of production for a single firm is much lower than the cost of production for competitive firms, this situation is called a / an",
# ["natural monopoly", "artificial monopoly", "oligopoly", "duopoly"],
# "natural monopoly"
# ),
# Question(
# "Costs that do not vary with the quantity of output produced are called",
# ["fixed costs", "variable costs", "marginal costs", "sunk costs"],
# "fixed costs"
# ),
# Question(
# "Costs that vary with the quantity of output produced are called",
# ["fixed costs", "variable costs", "marginal costs", "sunk costs"],
# "variable costs"
# ),
# Question(
# "The increase in output that arises from an additional unit of input is called",
# ["marginal product", "marginal profit", "marginal loss", "marginal cost"],
# "marginal product"
# ),

#         # Week 10
 
#         # Week 11
 
#         # Week 12
 
#     ]
    
#     if 'current_question' not in st.session_state:
#         st.session_state.current_question = 0
#         st.session_state.answers = {}
#         st.session_state.score = 0
#         st.session_state.test_completed = False
    
#     if not st.session_state.test_completed:
#         question = MOCK_TEST_QUESTIONS[st.session_state.current_question]
#         st.write(f"Question {st.session_state.current_question + 1}/{len(MOCK_TEST_QUESTIONS)}:")
#         st.write(question.text)
        
#         # Get previously selected answer for this question, if any
#         current_answer = st.session_state.answers.get(st.session_state.current_question)
        
#         # Pre-select the option if previously answered
#         index = question.options.index(current_answer) if current_answer in question.options else None
        
#         answer = st.radio(
#             "Select your answer:", 
#             options=question.options,
#             index=index,  # Will show previous selection if it exists
#             key=f"q_{st.session_state.current_question}"
#         )
        
#         if answer:
#             st.session_state.answers[st.session_state.current_question] = answer
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             if st.session_state.current_question > 0:
#                 if st.button("Previous"):
#                     st.session_state.current_question -= 1
#                     st.rerun()
        
#         with col2:
#             if st.session_state.current_question < len(MOCK_TEST_QUESTIONS) - 1:
#                 # Only show Next button if an answer is selected
#                 if answer:
#                     if st.button("Next"):
#                         st.session_state.current_question += 1
#                         st.rerun()
#                 else:
#                     st.button("Next", disabled=True)
#             else:
#                 # Only show Submit button if an answer is selected
#                 if answer:
#                     if st.button("Submit Test"):
#                         for i, q in enumerate(MOCK_TEST_QUESTIONS):
#                             if st.session_state.answers.get(i) == q.correct_answer:
#                                 st.session_state.score += 1
#                         st.session_state.test_completed = True
#                         st.rerun()
#                 else:
#                     st.button("Submit Test", disabled=True)
    
#     else:
#         st.success(f"Test completed! Your score: {st.session_state.score}/{len(MOCK_TEST_QUESTIONS)}")
#         if st.button("Retake Test"):
#             st.session_state.current_question = 0
#             st.session_state.answers = {}
#             st.session_state.score = 0
#             st.session_state.test_completed = False
#             st.rerun()
    
    st.sidebar.markdown('<br>' * 3, unsafe_allow_html=True)
    st.sidebar.image("qr.jpeg", width=300)
    st.sidebar.markdown('<div style="text-align: center;">Buy me a coffee ☕ :)</div>', unsafe_allow_html=True)
    
    create_footer()

if __name__ == "__main__":
    main()