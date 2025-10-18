# Test Design & Strategy

## Objective
Validate filtering, pagination, and negative flows in TMDB demo site using automated tests.

## Scope
- Filter by category (Popular, Trending, Top Rated)  
- Pagination functionality  
- Negative scenario (invalid URL)  
- Consistency where possible via API

## Test Design Techniques
- **Equivalence Partitioning**: choose representative categories  
- **Boundary**: test pagination edges  
- **Negative**: invalid URL, invalid filters

## Architecture
- Page Object Model (POM)  
- Config-driven setup  
- Setup/teardown via PyTest fixtures  
- Logging, screenshot capture  
- Timestamped reports  

## Execution
```bash
pip install -r requirements.txt
pytest
