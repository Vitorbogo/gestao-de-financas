import SearchBarComponent from '@/styles/components/searchBar'
import SideBarComponent from '@/styles/components/sidebar'
import {
  MainContainer,
  MainContent,
  MainWrapper,
  TitleContainer,
  TitleDiv,
  TopDiv,
} from '@/styles/pages'
import {
  Table,
  TableRow,
  TableHeader,
  TableCell,
} from '@/styles/pages/walletMain'
import Head from 'next/head'
import { useRouter } from 'next/router'

export default function Wallet() {
  const { query } = useRouter()

  return (
    <>
      <Head>
        <title>Wallet - Bongo Finance</title>
        <meta name='description' content='Wallet' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <MainWrapper>
        <SideBarComponent />
        <MainContainer>
          <TopDiv></TopDiv>
          <TitleContainer>
            <TitleDiv>
              <h1>Transações Recentes</h1>
            </TitleDiv>
            <SearchBarComponent />
          </TitleContainer>
          <MainContent>
            <Table>
              <thead>
                <TableRow>
                  <TableHeader>ID</TableHeader>
                  <TableHeader>Nome</TableHeader>
                  <TableHeader>Data</TableHeader>
                  <TableHeader>Status</TableHeader>
                  <TableHeader>Valor</TableHeader>
                </TableRow>
              </thead>
              <tbody>
                <TableRow>
                  <TableCell>1</TableCell>
                  <TableCell>John Doe</TableCell>
                  <TableCell>2021-05-20</TableCell>
                  <TableCell>Active</TableCell>
                  <TableCell>$100</TableCell>
                </TableRow>
                <TableRow>
                  <TableCell>2</TableCell>
                  <TableCell>Jane Smith</TableCell>
                  <TableCell>2021-05-21</TableCell>
                  <TableCell>Inactive</TableCell>
                  <TableCell>$200</TableCell>
                </TableRow>
              </tbody>
            </Table>
          </MainContent>
        </MainContainer>
      </MainWrapper>
    </>
  )
}
