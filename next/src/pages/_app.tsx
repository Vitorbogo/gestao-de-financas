import { globalStyles } from '@/styles/global'
import { AppProps } from 'next/app'

//Chama do global styles fora da function
// para ele não rodar toda vez que carregar uma página
globalStyles()

function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}

export default App
