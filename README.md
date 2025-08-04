# passg

## A simple Python password generator.

`passg` is a lightweight tool for generating secure and random passwords. It’s designed to be easy to use while ensuring strong password generation. With just one function, `generate_password`, you can create passwords of any length (with a minimum of 8 characters).

---

## Installation

Install `passg` using pip:

```bash
pip install passg
```

---

## Usage

Import the `generate_password` function and start generating passwords:

```python
from passg import generate_password

# Default 16-character password
password = generate_password()
print(password)

# Custom-length password (e.g., 50 characters)
password = generate_password(lenght=50)
print(password)
```

---

## Notes

- The minimum password length is 8 characters. If you try to generate a shorter password, `passg` will raise an error.
- The longer the password, the stronger it is!

---

## Example Outputs

Here are some example passwords:

- 16 characters: `aB3$fG7!kL9@mN2&`
- 20 characters: `xY4@zQ8!pL3$wR9%vT2*`
- 50 characters: `hJ6#kM1@qW4$eR7%tY8^uI0&oP3*lK9(nB2)mC5_dF4+gV7`

---

## Contributing

If you’d like to contribute or add features, feel free to open an issue or submit a pull request. All contributions are welcome!

---

## License

`passg` is open-source and released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

That’s it! `passg` is here to help you generate secure passwords quickly and easily :) 🔒
