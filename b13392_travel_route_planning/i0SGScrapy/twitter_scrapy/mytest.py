import twint
import nest_asyncio
c = twint.Config()
c.Username = "github"

# c.Proxy_host = "127.0.0.1"
# c.Proxy_port = 7890
# c.Proxy_type = "socks5"


c.Search = "code"
nest_asyncio.apply()
twint.run.Search(c)