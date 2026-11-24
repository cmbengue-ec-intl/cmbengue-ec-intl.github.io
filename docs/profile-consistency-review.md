# Portrait and professional-profile review — 24 November 2026

Prepared for owner review under #47. This branch is not a publication approval.

## Changes

- Restored `img/img1.jpg` byte-for-byte from the portrait selected for the ECI draft. SHA256: `cb0b542c7647a304733407d6910c2207a265a30df4105a0238c3680d782ca4d4`. The homepage, biography and social previews now use that portrait, with explicit dimensions and alternative text. A future commissioned portrait can replace this shared asset.
- Used the full professional name in site metadata and the header, with distinct page descriptions and a shared author/image configuration. The portrait keeps its natural aspect ratio, and the header can wrap on narrow screens.
- Preserved the settled titles and 2021 CliMA start dates from #42/#44. Added ecodesign's name and CliMA/ECI collaboration credit, and kept the software-team leadership description.
- Made recent IPCC expert-review service and the completed CUHK presentation discoverable from the homepage. Organised the biography into background, service and outside-work sections without changing the status of those activities.
- Added a three-paper selection above the complete bibliography and the explicit project-administration contribution to the 2026 CliMA entry. Earlier individual research is distinguished from ECI's company record.
- Corrected the static-stability paper's citation to the publisher's 2019 volume year and complete page range, while recording its 2018 online publication.
- Qualified the research page's hemisphere-wide storm-track assertion using the IPCC AR6 assessment. Added direct paper links to the research summary.
- Replaced obsolete West Point, Oxford Criminology and Monroe campus URLs with current institutional destinations and used HTTPS for education links. Extended the existing local-link checker to check fragment destinations. Repaired heading levels and chronology in the education/employment records, and added a homepage recovery link to the 404 page.

## Evidence

- Current personal-site baseline: `f1ad5ba`, including the settled titles in #44 and start-year correction in #42.
- ECI profile review: https://github.com/ec-intl/ecisite/pull/161. Names, roles, selected publications and service wording were reconciled with that reviewed draft and the owner's existing biography.
- Product scope and collaboration credit: https://ecodesign.clima.caltech.edu/server/.
- CliMA paper: https://doi.org/10.1029/2025MS005014. Contribution is project administration; no additional scientific or numerical contribution is inferred from coauthorship.
- Static-stability paper: https://link.springer.com/article/10.1007/s00382-018-4192-5. Volume 52, pages 1299–1315 (2019), first published online 2 April 2018.
- Hemisphere-specific storm-track assessment: https://www.ipcc.ch/report/ar6/wg1/chapter/technical-summary/.
- West Point catalogue: https://courses.westpoint.edu/fos_dept_catalog.cfm?str_sub_div_ofc_sym_cd=MADN-MAE&sub_id=996. This is a current programme link, not evidence that the present curriculum is identical to the historical degree.

## Validation and review limits

The Jekyll build passes in Ruby 3.3 on Linux. All nine generated pages pass local-link/fragment, image-alt and landmark checks. The seven main pages pass portrait/description metadata checks. Desktop homepage and 320 CSS-pixel homepage, biography and publications checks show loaded images and no horizontal overflow. These are targeted accessibility checks, not a full conformance audit. External publisher sites may block automated access; the thesis endpoint timed out. Those results are not treated as proof of broken links. The restored portrait's hash matches the ECI asset. No DNS, custom domain, account avatar or publication setting was changed. Publishing from `main` remains a separate owner decision. Existing dependency versions are retained, with Linux added to the platform lock for a reproducible local container build; this is a content, presentation and reference audit, not a dependency/security review. Private source correspondence and personal contact details are not bundled.
