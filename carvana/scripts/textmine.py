import re, pandas as pd
SELL=r"\b(sell|sold|selling|sale of my|instant offer|offer for my|their offer|carvana offer|appraisal|trade[- ]?in|traded in|picked up my car|pick up my car|pickup of my|payoff|buy my car|bought my car|sold my)\b"
BUY=r"\b(bought|buy|buying|purchas\w*|delivery|delivered|vending machine|financ\w*|7[- ]day|seven day|test own|return(ed)? (it|the car)|my new car)\b"
THEMES={
 'ease/convenience': r"\b(easy|easiest|simple|convenient|convenience|hassle|painless|seamless|smooth|quick|fast|from (my|the) (couch|home)|no pressure|stress[- ]free)\b",
 'price/offer value': r"\b(price|priced|pricing|offer|offered|more than|higher than|best deal|good deal|great deal|value|cheaper|overpriced|lowball|low ball)\b",
 'compares CarMax': r"\bcar ?max\b",
 'compares dealer': r"\b(dealer|dealership|dealerships|salesm[ae]n|car lot)\b",
 'compares KBB/Peddle/others': r"\b(kbb|kelley|peddle|vroom|cargurus|carfax|autotrader|facebook|marketplace|private (sale|party|buyer))\b",
 'financing/credit': r"\b(financ\w*|loan|interest|apr|rate|credit|down ?payment|bridgecrest|approved|pre-?qual\w*)\b",
 'delivery/pickup logistics': r"\b(deliver\w*|pick ?up|picked up|driver|hauler|vending|schedul\w*|resched\w*)\b",
 'title/registration/plates': r"\b(title|registration|register|plates?|temp(orary)? tags?|tags|dmv)\b",
 'mechanical/condition': r"\b(mechanic\w*|inspection|damage\w*|scratch\w*|dent\w*|check engine|repair\w*|broken|leak\w*|smell|tires?|recall)\b",
 'customer service': r"\b(customer service|advocate|support|communication|call(ed)? (them|carvana)|on hold|nobody|no one|email(ed)?|chat)\b",
 'offer cut at pickup': r"\b(lowered|reduced|dropped|changed|adjust\w*|deduct\w*|less than (the )?offer|renegotiat\w*)\b.*\b(offer|price)\b|\b(offer|price)\b.*\b(lowered|reduced|dropped|adjust\w*|deduct\w*)\b",
 'payoff/lender/negative equity': r"\b(payoff|pay off|lien\w*|lender|upside down|negative equity|owe more|gap)\b",
 'lease': r"\b(lease|leased|lessor|lease buyout|buyout)\b",
 'trust/scam': r"\b(trust\w*|legit|scam\w*|shady|honest|transparen\w*|fraud\w*|lied|lying)\b",
 'return/7-day': r"\b(7[- ]day|seven day|return(ed|ing)?)\b",
}
WHO={
 'military': r"\b(military|deploy\w*|pcs|stationed|army|navy|air force|marines?|veterans?|base|active duty|tdy)\b",
 'student/first car': r"\b(first car|first time buyer|first-time buyer|college|student|graduat\w*)\b",
 'family/kids': r"\b(my (wife|husband|son|daughter|kids?|family|baby|fianc\w*)|newborn|pregnan\w*|car seat)\b",
 'parent buying for kid': r"\b(for my (son|daughter|kid|teen)|my (16|17|18)[- ]year[- ]old)\b",
 'moving/relocation': r"\b(moved|moving|relocat\w*|cross[- ]country|out of state)\b",
 'retired/older': r"\b(retired|retirement|grandson|granddaughter|grandkids|senior|my 70|i'?m 6\d|i am 6\d)\b",
 'credit-challenged': r"\b(bad credit|poor credit|bankruptcy|repo\w*|subprime|low credit|credit (score )?of [45]\d\d)\b",
 'EV/Tesla': r"\b(tesla|model 3|model y|ev|electric|bolt|leaf|ioniq|mach-?e)\b",
 'truck': r"\b(truck|f-?150|silverado|sierra|ram 1500|tacoma|tundra|pickup truck)\b",
 'new job/commute': r"\b(new job|commute|commuting|work truck)\b",
}
def tag(df, textcol='text'):
    t=df[textcol].fillna('').str.lower()
    df['is_sell']=t.str.contains(SELL,regex=True)
    df['is_buy']=t.str.contains(BUY,regex=True)
    df['side']=pd.Series(pd.NA,index=df.index,dtype=object)
    df.loc[df.is_sell&~df.is_buy,'side']='seller'
    df.loc[df.is_buy&~df.is_sell,'side']='buyer'
    df.loc[df.is_buy&df.is_sell,'side']='both'
    df['side']=df['side'].fillna('unclear')
    for k,v in {**THEMES,**WHO}.items():
        df[k]=t.str.contains(v,regex=True)
    return df
