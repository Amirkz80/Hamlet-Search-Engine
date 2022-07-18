import { useEffect, useRef } from "react"
import { SearchIcon } from "@heroicons/react/solid"

const SearchBar = ({ value, handleClick, handleChange }) => {
  const inputRef = useRef()

  useEffect(() => {
    inputRef.current.select()
  }, [])

  return (
    <div className="flex p-2 w-1/2 rounded-full border-2 border-gray-200 hover:border-gray-300 hover:shadow">
      <button onClick={handleClick}>
        <SearchIcon className="h-6 text-gray-400 hover:cursor-pointer hover:text-gray-600" />
      </button>
      <input
        className="ml-2 w-full outline-none text-left"
        type="text"
        ref={inputRef}
        value={value}
        onChange={handleChange}
      />
    </div>
  )
}

export default SearchBar
