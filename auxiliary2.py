sumlist_ind = ["eng", "age", "female", "white" , "black" , "asianpi"  , "other",  "multi" , "hispdum" ,"yrssch", "marriedpresent" ,"divorced" ,"evermarried", "nchild", "haskid" ,"singleparent" ,"nevermarried_haskid", "share_bpld_minusself" ,"abovemean_bpld2" ,"ancestpct_minusself" ,"abovemean_ancestry2" ,"nengdom", "young9","perwt2" ]
sumlist_mat = ["spouseeng", "marriednative" ,"couplesamebpld", "couplesameancestry1", "spouseage", "spouseyrssch" ,"yrssch" ,"spouselnwage", "spouseworkedly" ,"bothworked" ,"nchild" ,"haskid", "nengdom", "young9","perwt2"]



list_table2_ind = ["eng1","eng2", "eng3", "eng","marriedpresent", "divorced","evermarried" ,
       "nchild",
         "haskid" ,
        "singleparent","nevermarried_haskid" ,
         "share_bpld_minusself",
         "abovemean_bpld2" ,
"ancestpct_minusself", "abovemean_ancestry2"]

list_table2_mat = ["spouseeng", "marriednative", "couplesamebpld", "couplesameancestry1","spouseage","spouseyrssch"
     ,"spouselnwage"
    ,"spouseworkedly"
    ,"bothworked"
    ,"nchild_spouse", "haskid_spouse" ]

# dictionary = dict ([
#     (  "eng1" , "Speaks English not well or better" ),
#      (  "eng2" , "Speaks English well or better" ),
#       ( "eng3"  , "Speaks English very well"  ),
#     ("eng" , "English-speaking ability ordinal measure"  ),
#      ( "marriedpresent",  "Is currently married with spouse present"  ),
#       ( "divorced" , "Is currently divorced"  ),
#       ( "evermarried" ,  "Has ever married"  ),
#      (  "spouseeng", "Spouse English-speaking ability ordinal measure"   ),
#        ("marriednative", "Spouse is US-born"),
#        ("couplesamebpld", "Spouse has the same country of birth"),
#      ("couplesameancestry1", "Spouse has the same ancestry"),
#       ("spouseage" , "Spouse age"),
#       ("spouseyrssch", "Spouse years of schooling"),
#        ("spouselnwage", "Spouse log(wages last year)"),
#        ("spouseworkedly", "Spouse worked last year" ),
#         ("bothworked", "Both worked last year"),
#          ("nchild", "Number of children living in same household"),
#           ("haskid", "Has a child living in same household"),
#          ("nchild_spouse", "Number of children living in same household, only individuals married spouse present"),
#         ( "haskid_spouse", "Has a child living in same household, only individuals married with spouse present"),
#      ( "singleparent" , "Is a single parent"),
#      (  "nevermarried_haskid", "Is a never married, single parent" ),
#       ( "share_bpld_minusself", "Fraction of PUMA population from same country of birth" ),
#      ( "abovemean_bpld2" ,  "Fraction from same country of birth is above national mean for the country of birth"),
#     ( "ancestpct_minusself", "Fraction of PUMA population with same primary ancestry" ),
#       ( "abovemean_ancestry2" , "Fraction with same ancestry is above national mean for the primary ancestry")

# ])

list_table3_ind = ["marriedpresent"
    ,"divorced"
    , "evermarried"
    , "nchild"
    , "haskid"
    , "singleparent"
    , "nevermarried_haskid"
    , "share_bpld_minusself"
    , "abovemean_bpld2"
    , "ancestpct_minusself"
    , "abovemean_ancestry2"
            ]
list_table3_mat = ["spouseeng", "marriednative", "couplesamebpld", "couplesameancestry1","spouseage","spouseyrssch"
     ,"spouselnwage"
    ,"spouseworkedly"
    ,"bothworked"
    ,"nchild_spouse", "haskid_spouse"    ]


Dict_for_sumlist1 = dict ([
    ("eng" , "English-speaking ability ordinal measure" ),
    ("age", "Age"),
    ("female", "Female"),
    ("white", "White"),
    ("black", "Black"),
    ("asianpi", "Asian/Pacific Islander"),
    ("other", "Other single race"),
    ("multi", "Multiracial"),
    ("hispdum", "Hispanic"),
    ("yrssch", "Years of schooling"),
    ( "marriedpresent",  "Is currently married with spouse present"  ),
      ( "divorced" , "Is currently divorced"  ),
      ( "evermarried" ,  "Has ever married"  ),
     (  "spouseeng", "Spouse English-speaking ability ordinal measure"   ),
       ("marriednative", "Spouse is US-born"),
       ("couplesamebpld", "Spouse has the same country of birth"),
     ("couplesameancestry1", "Spouse has the same ancestry"),
      ("spouseage" , "Spouse age"),
      ("spouseyrssch", "Spouse years of schooling"),
       ("spouselnwage", "Spouse log(wages last year)"),
       ("spouseworkedly", "Spouse worked last year" ),
        ("bothworked", "Both worked last year"),
         ("nchild", "Number of children living in same household"),
          ("haskid", "Has a child living in same household"),
         ("nchild_spouse", "Number of children living in same household, only individuals married spouse present"),
        ( "haskid_spouse", "Has a child living in same household, only individuals married with spouse present"),
     ( "singleparent" , "Is a single parent"),
     (  "nevermarried_haskid", "Is a never married, single parent" ),
      ( "share_bpld_minusself", "Fraction of PUMA population from same country of birth" ),
     ( "abovemean_bpld2" ,  "Fraction from same country of birth is above national mean for the country of birth"),
    ( "ancestpct_minusself", "Fraction of PUMA population with same primary ancestry" ),
      ( "abovemean_ancestry2" , "Fraction with same ancestry is above national mean for the primary ancestry")
])

Dict_for_sumlist2 = dict ([
    ( "English-speaking ability ordinal measure" ,"Panel A. Regressors"),
    ("Age","Panel A. Regressors"),
    ("Female","Panel A. Regressors"),
    ("White","Panel A. Regressors"),
    ("Black", "Panel A. Regressors"),
    ("Other", "Panel A. Regressors"),
    ("Asian/Pacific Islander","Panel A. Regressors"),
    ( "Multi","Panel A. Regressors"),
    ( "Hispdum","Panel A. Regressors"),
    ("Years of schooling","Panel A. Regressors"),
    (  "Is currently married with spouse present" ,"Panel B. Marriage outcomes" ),
      (  "Is currently divorced" ,"Panel B. Marriage outcomes" ),
      (   "Has ever married" ,"Panel B. Marriage outcomes" ),
     (  "Spouse English-speaking ability ordinal measure"  ,"Panel B. Marriage outcomes" ),
       ( "Spouse is US-born","Panel B. Marriage outcomes"),
       ( "Spouse has the same country of birth","Panel B. Marriage outcomes"),
     ("Spouse has the same ancestry","Panel B. Marriage outcomes"),
      ( "Spouse age","Panel B. Marriage outcomes"),
      ( "Spouse years of schooling","Panel B. Marriage outcomes"),
       ( "Spouse log(wages last year)","Panel B. Marriage outcomes"),
       ("Spouse worked last year" ,"Panel B. Marriage outcomes"),
        ("Both worked last year","Panel B. Marriage outcomes"),
         ( "Number of children living in same household", "Panel C. Fertility outcomes"),
          ("Has a child living in same household", "Panel C. Fertility outcomes"),
         ( "Number of children living in same household, only individuals married spouse present", "Panel C. Fertility outcomes"),
        (  "Has a child living in same household, only individuals married with spouse present", "Panel C. Fertility outcomes"),
     ( "Is a single parent", "Panel C. Fertility outcomes"),
     (  "Is a never married, single parent", "Panel C. Fertility outcomes" ),
      (  "Fraction of PUMA population from same country of birth", "Panel D. Residential location outcomes" ),
     ( "Fraction from same country of birth is above national mean for the country of birth", "Panel D. Residential location outcomes"),
    (  "Fraction of PUMA population with same primary ancestry", "Panel D. Residential location outcomes" ),
      (  "Fraction with same ancestry is above national mean for the primary ancestry", "Panel D. Residential location outcomes")
    
    
])




