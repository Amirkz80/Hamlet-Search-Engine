const TopBar = ({ children }) => {
  return (
    <div className="flex justify-center p-3 top-0 sticky z-50 bg-white">
      {children}
    </div>
  )
}

export default TopBar
