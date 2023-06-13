import { SearchBar, SearchButton, SearchInput } from '../pages/searchBar'
import Image from 'next/image'

import SearchImg from '../../assets/search.svg'

export default function SearchBarComponent() {
  return (
    <SearchBar>
      <SearchInput type='text' placeholder='Search...' />
      <SearchButton>
        <Image src={SearchImg} alt='Procurar' width={28} height={28} />
      </SearchButton>
    </SearchBar>
  )
}
