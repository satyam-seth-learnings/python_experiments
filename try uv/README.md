- [Official Doc Link](https://docs.astral.sh/uv/)

- [YouTube Video Link](https://youtu.be/8mk85fyzevc?si=1Fo1NRkWB6d5KjcI)


- Run module with dependencies
```bash
uv run --with 'flask' --with 'requests' chaiexample.py 
```

- Add dependencies script for the module
```bash
uv add --script chaiexample.py 'flask' 'requests' 
```