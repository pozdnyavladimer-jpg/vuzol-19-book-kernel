# 228A — SIX COLOR HEIGHTS / BLIND SPECTRAL PARTITION TEST

**Status:** synthetic physiology-grounded falsification test.

## Known constraints used
Human photopic color encoding begins with three broad overlapping S/M/L cone responses. The visible spectrum is continuous and does not contain six objectively separated color bins.

This toy model therefore asks a narrower question:

> If a continuous wavelength axis is represented by overlapping S/M/L-like responses plus opponent coordinates, is K=6 a useful data-driven compression?

It does NOT ask whether nature contains exactly six fundamental colors.

## Model
Wavelength grid: 380–780 nm, 1 nm steps.

Approximate cone-like peaks:
- S ≈ 445 nm
- M ≈ 535 nm
- L ≈ 565 nm

Derived opponent coordinates:
- red/green-like: `L-M`
- blue/yellow-like: `S-(L+M)/2`

For each K=2…12, dynamic programming finds the globally best K contiguous wavelength bands under within-band squared error.

## Search
|   K bands |   Within-band SSE |   Explained spectral structure |   Marginal gain |
|----------:|------------------:|-------------------------------:|----------------:|
|         2 |         1659.43   |                       0.310293 |    nan          |
|         3 |          716.912  |                       0.702032 |      0.391738   |
|         4 |          427.645  |                       0.822259 |      0.120227   |
|         5 |          314.268  |                       0.869381 |      0.0471222  |
|         6 |          240.29   |                       0.900129 |      0.0307476  |
|         7 |          169.571  |                       0.929521 |      0.0293926  |
|         8 |          128.457  |                       0.94661  |      0.0170883  |
|         9 |          101.436  |                       0.95784  |      0.0112306  |
|        10 |           82.96   |                       0.96552  |      0.00767916 |
|        11 |           69.9709 |                       0.970918 |      0.00539865 |
|        12 |           60.2643 |                       0.974952 |      0.00403432 |

## Complexity penalty
|   K bands |   BIC-like score (lower better) |
|----------:|--------------------------------:|
|         2 |                        -800.374 |
|         3 |                       -2772.97  |
|         4 |                       -3969.34  |
|         5 |                       -4663.78  |
|         6 |                       -5262.84  |
|         7 |                       -6054.79  |
|         8 |                       -6676.17  |
|         9 |                       -7197.67  |
|        10 |                       -7634.73  |
|        11 |                       -7997.71  |
|        12 |                       -8310.3   |

## Blind K=6 boundaries
|   Band |   Start nm |   End nm |      S mean |     M mean |    L mean |        L-M |   S-(L+M)/2 |
|-------:|-----------:|---------:|------------:|-----------:|----------:|-----------:|------------:|
|      1 |        380 |      475 | 0.710638    | 0.109001   | 0.04781   | -0.0611908 |   0.632232  |
|      2 |        476 |      508 | 0.417232    | 0.632085   | 0.351344  | -0.280741  |  -0.0744828 |
|      3 |        509 |      555 | 0.0634952   | 0.954429   | 0.787772  | -0.166656  |  -0.807605  |
|      4 |        556 |      597 | 0.00164965  | 0.649725   | 0.947458  |  0.297733  |  -0.796942  |
|      5 |        598 |      644 | 1.2279e-05  | 0.179877   | 0.538467  |  0.35859   |  -0.359159  |
|      6 |        645 |      780 | 3.85993e-09 | 0.00620324 | 0.0515207 |  0.0453174 |  -0.0288619 |

Candidate opponent zero-crossing Gates:
`{'L-M zero crossings (nm)': [549.5], 'Blue-yellow opponent zero crossings (nm)': [488.5]}`

## Interpretation
Six bands can be a useful discretization if they preserve much of the spectral-response geometry with modest complexity. But K=6 is not automatically a physical constant. A larger K must reconstruct the continuous curves better; the relevant question is whether additional bands buy enough information to justify their complexity.

This gives a cleaner Vuzol-19 mapping:

`Height = location/scale on a continuous spectral coordinate`

`Direction = sign/orientation in an opponent or phase coordinate`

`Gate = crossing/threshold where the response regime changes`

`Rune = operation performed at that coordinate`

Thus a "color" can be treated as a coarse Height region, while the Gate lies at transitions between response regimes.

## Anti-PRION
ALLOW: discrete color-height bands are useful compression coordinates.
ALLOW: opponent sign changes provide natural transition/Gate candidates.
HOLD: six bands are privileged.
BLOCK: six colors are six fundamental physical wave states.
