# Async task

## Architecture overview

### The application is comprised of 3 components:
- streams
- stream_operators
- stream_reporter

### Component overview
#### streams
Receives the network data and packages it in the form of a flat list. (1 API call / 1 flat list).

#### stream_operators
A class comprised of static methods performing various filtering tasks.

#### stream_reporter
Displays the data readout and sets the ordering of the filtering methods.